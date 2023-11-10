import json

def count_genres(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            data = file.read()

            movies = [line.split('::') for line in data.split('\n') if line]

            genre_count = {}

            for movie in movies:
                genres = movie[2].split('|')
                for genre in genres:
                    genre_count[genre] = genre_count.get(genre, 0) + 1

            return genre_count

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return None

def write_result(output_file, genre_count):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for genre, count in genre_count.items():
                file.write("{} {}\n".format(genre, count))

        print("Results written to {}".format(output_file))

    except Exception as e:
        print("Error writing to {}: {}".format(output_file, e))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 장르별 영화 수 계산
    genre_count = count_genres(input_file)

    if genre_count is not None:
        # 결과를 출력 파일에 쓰기
        write_result(output_file, genre_count)
