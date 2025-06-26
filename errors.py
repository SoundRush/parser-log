import re

def get_statuses_from_user():
    user_input = input("Введи коды статусов (например: 500-504 404 200): ")
    statuses = set()
    for part in user_input.split():
        if '-' in part:
            start, end = map(int, part.split('-'))
            statuses.update(range(start, end + 1))
        else:
            statuses.add(int(part))
    return statuses

def count_statuses_in_log(file_path, statuses):
    counts = {status: 0 for status in statuses}
    status_pattern = re.compile(r'\b(\d{3})\b')

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                matches = status_pattern.findall(line)
                for match in matches:
                    code = int(match)
                    if code in statuses:
                        counts[code] += 1
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None

    return counts

def main():
    file_path = "all_logs/server_errors.log"
    statuses = get_statuses_from_user()
    result = count_statuses_in_log(file_path, statuses)

    if result:
        print("\nРезультат:")
        for code in sorted(result.keys()):
            print(f"Статус {code}: {result[code]} раз")

if __name__ == "__main__":
    main()