
class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall_obj):
        cls.__hall_list.append(hall_obj)


class Hall(Star_Cinema):
    movie_id = []

    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.movie_id.append(id)
        movie_details = (id, movie_name, time)
        self.__show_list.append(movie_details)
        self.__seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, id, seats_to_book):
        if id in self.movie_id:
            seat_map = self.__seats[id]
            for seat in seats_to_book:
                row, col = seat
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if seat_map[row][col] == 0:
                        seat_map[row][col] = 1
                        print(f'Seat No:({row}, {col}) Booked Successfully in Hall No. {self.hall_no} for show {id}')
                    else:
                        print('Seat is Booked')
                else:
                    print('Invalid Seat Choosen')
        else:
            print(f'Invalid Show ID: {id}, available Show IDs Are: {self.movie_id}')

    def view_show_list(self):
        print('--------------------------------')
        for show in self.__show_list:
            print(f'MOVIE NAME: {show[1]} SHOW ID: {show[0]} TIME: {show[2]}') 
        print('--------------------------------')
        
    def view_available_seats(self, id):
        if id in self.movie_id:
            print()
            print(f"Seat map for movie ID {id}:")
            for row in self.__seats[id]:
                print(row)
            print('\n-----SCREEN-----\n')
        else: 
            print("\nInvalid Show Id\n")
        
    def __repr__(self):
        return f'Hall {self.hall_no}: {self.rows}x{self.cols}'

hall1 = Hall(5, 5, 102)
hall2 = Hall(3, 3, 103)
hall1.entry_show(110, "Avengers: Infinity War", "10:00 AM")
hall1.entry_show(120, "Avengers: Endgame  War", "2:00 PM")




while True:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT')
    opt=int(input("ENTER OPTION: "))
    if opt==1:
        hall1.view_show_list()
    elif opt==2:
        show_id=int(input("ENTER SHOW ID: "))
        hall1.view_available_seats(show_id)
    elif opt == 3:
        shw_id = int(input("Show ID: "))
        if shw_id in Hall.movie_id:  
            tick_need = int(input("Number of Tickets?: "))
            for _ in range(tick_need):
                row = int(input("Enter Seat Row: "))
                col = int(input("Enter Seat Col: "))
                hall1.book_seats(shw_id, [(row, col)])
        else:
            print(f'\nInvalid Show ID: {shw_id}, available Show IDs Are: {Hall.movie_id}\n')
    elif opt == 4:
        break
    else:
        print('\nWrong Option Entered\n')
