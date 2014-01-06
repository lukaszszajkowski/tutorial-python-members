

def add_some_values(value1, value2):
    result = value1 + value2
    return result


class Member(object):                               # Always inherit from object
    'Common base class for all members'             # Document your classes
    member_count = 0                                # Public Static variable

    def __init__(self, forename, refno):             # Constructor
        self.forename = forename                      # Public variable
        self.__refno = refno                        # Private variable
        Member.member_count += 1

    def get_refno(self):                            # Public method
        return self.__refno

