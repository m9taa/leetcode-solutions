import itertools
import os
import tempfile

from collections.abc import Iterator
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import click
import requests


LEETCODE_GRAPHQL_ENDPOINT = 'https://leetcode.com/graphql'
ROOT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = {
    'filepath': ROOT_DIR.joinpath('README.md'),
    'offset': 6,
    'sep': '  |  ',
}
LANG_TO_EXTENSION = {
    'C++': '.cpp',
    'Python': '.py',
}


def _get_problem_info(link: str) -> Dict[str, Any]:
    url_path = requests.utils.urlparse(link).path.split('/')
    if len(url_path) > 4 or url_path[1] != 'problems':
        raise ValueError(f'Input link is not correct: {link}.')

    problem_name = url_path[2]
    query = '''query {
        question(titleSlug: "''' + problem_name + '''") {
            questionId
            title
            titleSlug
            difficulty
            topicTags {
                name
            }
        }
    }
    '''
    data = requests.post(LEETCODE_GRAPHQL_ENDPOINT, json={'query': query})
    res = data.json()['data']['question']
    if not res:
        raise Exception("Something went wrong, maybe input link is not correct.")
    return res


def generate_solution_files(problem_info: Dict[str, Any]) -> Dict[str, str]:
    # Create files for future solutions
    filepaths = {}
    for lang, fileext in LANG_TO_EXTENSION.items():
        filepath = '/'.join((lang, problem_info['titleSlug'] + fileext))
        abs_path = ROOT_DIR.joinpath(filepath)
        try:
            if abs_path.exists():
                raise Exception(f'Solution file exists: {filepath}')
        except Exception as e:
            for fpath in filepaths.values():
                os.remove(fpath)
            raise e
        with open(abs_path, 'a'):
            pass
        filepaths[lang] = filepath
    return filepaths


def generate_new_record(link: str, problem_info: Dict[str, Any], filepaths: Dict[str, str]) -> List[str]:
    # Generate record for output table
    output_row = [
        str(problem_info['questionId']),  # №
        f'[{problem_info["title"]}]({link})',  # Title
        ' / '.join(f'[{lang}]({filepath})' for lang, filepath in filepaths.items()),  # Solution
        '?',  # Time
        '?',  # Space
        problem_info['difficulty'],  # Difficulty
        ', '.join(map(lambda d: d['name'], problem_info['topicTags'])),  # Note
    ]
    return output_row


def _binary_search(nums: List[int], target_num: int) -> Tuple[str, bool]:
    if not nums:
        return -1, False

    start, end = 0, len(nums)
    while start < end - 1:
        m = (start + end) // 2
        if nums[m] > target_num:
            end = m
        else:
            start = m
    return start, nums[start] == target_num


def check_table_for_solution(file_info: Dict[str, Any], problem_num: int) -> int:
    solved_problems = []
    with open(file_info['filepath']) as fd:
        for line in itertools.islice(fd, file_info['offset'], None):
            solved_num = int(line.split('|', 2)[1].strip())
            solved_problems.append(solved_num)
    return _binary_search(solved_problems, problem_num)


def _insert_line(lines: Iterable, insert_index: int, line_to_insert: str) -> Iterator:
    lines = iter(lines)
    i = 0
    for i, line in enumerate(itertools.islice(lines, insert_index)):
        yield line
    if insert_index > i + 1:
        raise ValueError('Insert index is beyond `lines`')
    yield line_to_insert
    yield from lines


def update_file(file_info: Dict[str, Any], record: str, insertion_index: int) -> None:
    tmp_file_name = next(tempfile._get_candidate_names())
    tmp_file = ROOT_DIR.joinpath(tmp_file_name)
    try:
        with open(file_info['filepath'], 'r') as fd_in, open(tmp_file, 'w') as fd_out:
            output_lines = _insert_line(fd_in, file_info['offset'] + insertion_index + 1, record)
            fd_out.writelines(output_lines)
        tmp_file.replace(file_info['filepath'])
    except Exception as e:
        if os.path.exists(tmp_file):
            os.remove(tmp_file)
            raise e


@click.command()
@click.option('--link', '-l',
              required=True,
              help='-link https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/',
              )
def add_new_solution(link: str) -> None:
    problem_info = _get_problem_info(link)
    insertion_index, exists = check_table_for_solution(OUTPUT_FILE, int(problem_info['questionId']))
    if exists:
        raise Exception(f'Solution for this problem exists: problem number {problem_info["questionId"]}.')

    code_filepaths = generate_solution_files(problem_info)
    record = generate_new_record(link, problem_info, code_filepaths)
    readme_record = '|  ' + OUTPUT_FILE['sep'].join(record) + '  |\n'
    update_file(OUTPUT_FILE, readme_record, insertion_index)


if __name__ == '__main__':
    add_new_solution()
