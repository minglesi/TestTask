import re
import argparse
import glob


def find_phones(text):
    regxs = [
        # country and area code
        re.compile(r"(\+*(\d{1,3})[ -]*(\d{3})[ -]*(\d{7}|\d{3}-\d{4}|\d{3}-\d{2}-\d{2}))"),
        re.compile(r"(\+*(\d{1,3}) \((\d{3})\) (\d{7}|\d{3}-\d{4}|\d{3}-\d{2}-\d{2}))"),
        # area code
        re.compile(r"((\d{3})[ -]*(\d{7}|\d{3}-\d{4}|\d{3}-\d{2}-\d{2}))"),
        re.compile(r"(\((\d{3})\) (\d{7}|\d{3}-\d{4}|\d{3}-\d{2}-\d{2}))"),
        # only number
        re.compile(r"(\d{7}|\d{3}-\d{4}|\d{3}-\d{2}-\d{2})")
    ]
    matches = set()
    for r in regxs:
        for match in r.findall(text):
            matches.add(match)
            text = text.replace(match[0], "")
    result = set()
    for match in matches:
        if len(match) == 4:
            # country and area code
            country = match[1]
            area = match[2]
            number = match[3].replace("-", "")
        elif len(match) == 3:
            # area code
            country = "7"
            area = match[1]
            number = match[2].replace("-", "")
        else:
            # only number
            country = "7"
            area = "812"
            number = match.replace("-", "")
        number = number[:3] + "-" + number[3:]
        result.add(f"+{country} ({area}) {number}")
    return result


def get_files(path):
    return glob.glob(path+"/**/*.txt", recursive=True)


def main(path):
    files = get_files(path)
    result = set()
    for path in files:
        with open(path, 'r') as file:
            text = file.read()
            result.update(find_phones(text))
    result = sorted(list(result))
    for r in result:
        print(r)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Phone Numbers Formatting', description='Given a directory ')
    parser.add_argument('path')
    args = parser.parse_args()
    main(args.path)
