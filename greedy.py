from main import main

from statistics import mean


class Search:
    def __init__(self, books, libraries, no_days):
        self.books_processed = {}
        self.libraries_remaining = []
        self.processed_libraries = []
        for library in libraries:
            self.libraries_remaining.append(library)
        self.days_remaining = no_days

    def greedy_search(self):
        while (self.days_remaining > 0 and len(self.libraries_remaining) > 0):
            self.iteration(self.libraries_remaining)
        return self.processed_libraries


    def iteration(self,libraries):
        local_scores = []
        max_score = -1
        best_lib = -1
        for idx, library in enumerate(libraries):
            score = self.get_local_score(library)
            if score > max_score:
                max_score = score
                best_lib = idx
            local_scores.append(score)
        self.sign_up(libraries[best_lib])
        del self.libraries_remaining[best_lib]


    def sign_up(self,library):
        unique_books = self.get_unique_books(library.books_in)
        for book in unique_books:
            self.books_processed[book] = library

        self.days_remaining -= library.time_to_signup
        self.processed_libraries.append(library)


    def get_unique_books(self,books):
        unique_books = []
        for book in books:
            if book not in self.books_processed:
                unique_books.append(book)
        return unique_books


    def get_local_score(self, library):
        books = library.books_in
        unique_books = self.get_unique_books(books)
        mean_score_unique_books = mean(unique_books)
        number_of_books_per_day =-1
        number_of_books_in_library = -1
        signup_time = -1

        score =  (mean_score_unique_books * number_of_books_in_library * number_of_books_per_day) / signup_time
        return score


if __name__ == "__main__":
    books, libraries, no_days = main()
    search = Search(books, libraries, no_days) 
    libraries = search.greedy_search()
    print('done')
    print(libraries)
