import re
import argparse
import glob

phone_regxp = re.compile(r"(?:^|[,. ])(?:\+(\d{1,3})(?: ?(\d{3}) ?| \((\d{3})\) )|(\d{1,3})-(\d{3})-)(\d{7}|\d{3}-\d{4}|\d{3}-\d{2}-\d{2})(?:$|[,. ])|"
                         r"(?:^|[,. ])(?:(\d{3})[ -]?|\((\d{3})\) )(\d{7}|\d{3}-\d{4}|\d{3}-\d{2}-\d{2})(?:$|[,. ])|"
                         r"(?:^|[,. ])(\d{7}|\d{3}-\d{4}|\d{3}-\d{2}-\d{2})(?:$|[,. ])")


def find_phones(text):
    result = set()
    for match in phone_regxp.findall(text):
        match = [m for m in match if m != ""]
        country = "7"
        area = "812"
        if len(match) == 3:
            # country and area code
            country = match[0]
            area = match[1]
            number = match[2].replace("-", "")
        elif len(match) == 2:
            # area code
            area = match[0]
            number = match[1].replace("-", "")
        else:
            # only number
            number = match[0].replace("-", "")
        result.add(int(country + area + number))
    return result


def get_files(path):
    return glob.glob(path + "/**/*.txt", recursive=True)


def main(path):
    print(f"Searching in path: {path}")
    files = get_files(path)
    print(f"Found {len(files)} files.")
    result = set()
    for path in files:
        with open(path, 'r') as file:
            for line in file:
                result.update(find_phones(line))
    result = sorted(list(result))
    print("\nPrinting results:")
    for r in result:
        r = str(r)
        number = "+" + r[:-10] + " (" + r[-10:-7] + ") " + r[-7:-4] + "-" + r[-4:]
        print(number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Phone Numbers Formatting', description='Given a directory with text files, '
                                                                                  'finds and gives the desire format '
                                                                                  'to the '
                                                                                  'telephone numbers in it')
    parser.add_argument('path')
    args = parser.parse_args()
    main(args.path)
