# hw10pr1.py 
#
# Name:
#

# First, the class definition
#
# ++ ALSO ++  below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # The constructor is always named __init__ !
    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    # The "printing" function is always named __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        d = self.day
        m = self.month
        y = self.year
        string = f"{m:02d}/{d:02d}/{y:04d}"
        # The "d" after the integer stands for "_d_ecimal integer..."
        return string

        #
        # Note that we could have also written:
        #
        # return f"{self.month:02d}/{self.day:02d}/{self.year:04d}"


    # Here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """Decides whether self and d2 represent the same calendar date,
           regardless of whether they are in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
                    and self.day == d2.day:    # The backslash allows this on a new line!
            return True
        else:
            return False
        
    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
           in history as ==.  This way , we don't need to use the awkward
           d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month \
               and self.day == d2.day:
            return True
        else:
            return False
        
    def isBefore(self, d2):
        '''usage: isBefore(self, d2) returns True if the calling object is a calendar date before the argument named d2'''
        if self.year < d2.year:
            return True
        elif self.month < d2.month and self.year == d2.year:
            return True
        elif self.day < d2.day and self.month == d2.month and self.year == d2.year:
            return True
        else:
            return False

    def __lt__(self, d2):
        """Overrides the < operator so that it declares two of the same dates
           in history as <.  This way , we don't need to use the awkward
           d.equals(d2) syntax...
        """
        if self.isBefore(d2):
            return True 
        else:
            return False
    
    def isAfter(self, d2):
        '''usage: isAfter(self, d2) returns True if the calling object is a calendar date after the argument named d2'''
        if self < d2:
            return False
        elif self == d2:
            return False
        else:
            return True
    
    def __gt__(self, d2):
        """Overrides the > operator so that it declares two of the same dates
           in history as >.  This way , we don't need to use the awkward
           d.equals(d2) syntax...
        """
        if self.isAfter(d2):
            return True 
        else:
            return False
        
    def tomorrow(self):
        """change the calling object so that it represents one calendar day after the date it originally represented"""
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28

        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day += 1
        if self.day > DIM[self.month]:    # We've gone past the end of this month: switch!
            self.day = 1
            self.month += 1

            # We need to check if the month has gone past the end of the year!!!
        if self.month > len(DIM) - 1:
                self.day = 1
                self.month = 1
                self.year += 1

    def yesterday(self):
        """ changes the calling object so that it represents one calendar before after the date it originally represented! """
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28

        # be sure to define fdays here (perhaps use an if - or the "Luke" trick!)
        DIM = [31, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        self.day -= 1
        if self.day <= 0:   # We've wrapped to the previous month!
            self.month -= 1
            self.day = DIM[self.month]

        if self.month < 1:
            self.month = 12
            self.day = DIM[self.month]
            self.year -= 1

    def addNDays(self, N):
        '''usage: addNDays(self, N)
         changes the calling object so that it represents N calendar days after the date it originally represented '''
        print(self)
        for x in range(N):
            self.tomorrow()
            print(self)


    def subNDays(self, N):
        '''usage: subNDays(self, N)
         changes the calling object so that it represents N calendar days before the date it originally represented '''
        print(self)
        for x in range(N):
            self.yesterday()
            print(self)

    def diff(self, d2):
        '''usage: diff(self, d2)
        returns the difference between any two dates'''
        d2copy = d2.copy()
        iterations = 0

        if d2copy > self:
            while d2copy != self:
                d2copy.yesterday()
                iterations += -1
        
        elif d2copy < self:
            while d2copy != self:
                d2copy.tomorrow()
                iterations += 1

        else:
            iterations = 0

        return iterations
    
    def dow(self):
        '''Usage: dow(self)
        returns a string that indicates the day of the week (dow) of the object (of type Date) that calls it.'''
        bigweeklist = ['Sunday','Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']
        dsunday = Date(10, 10, 2010)
        newvar = self.diff(dsunday)
        newday = newvar % 7
        return bigweeklist[newday]
#  
# Be sure to add code for the Date class ABOVE--indented inside the class
# definition
#

#
# Lots of dates to work with...
#
# The nice thing about putting them here is that they get redefined with
#   each run of the software (needed for testing!)
#

d = Date(4, 5, 2023)     # Today? Yesterday?
d2 = Date(5, 13, 2023)    # Start of summer break
ny = Date(1, 1, 2024)     # New year
nd = Date(1, 1, 2030)     # New decade
nc = Date(1, 1, 2100)     # New century
graduation = Date(5, 16, 2026)    # Alter to suit!
nextsemester = Date(8, 28, 2023)  # Start of classes next semester
wd = Date(11, 12, 2013)   # A popular wedding day
wd2 = Date(11, 12, 2013)  # A copy of wd, to check == and .equals()
wd10 = Date(10, 10, 2010)  # 10/10/10
sm1 = Date(10, 28, 1929)  # One stock market crash
sm2 = Date(10, 19, 1987)  # Another crash: October Mondays are risky!
