class Validator():

    def __init__(self, controller):
        self.controller = controller

    def validate_play(self, args):
        """Validates the play command.
        """
        # TODO: check if first thing is a sound or flag (maybe)
        if not args:
            return False
        return True
        
    def validate_rename(self, args):
        """Validates the rename command.
        """
        # TODO: think if there's other things we need to validate
        input = args.split(" ")
        if len(input) == 2:
            return True
        return False
        
    def validate_list_sounds(self, args):
        """Validates the list_sounds command.
        """
        # TODO: think if there's other things we need to validate
        input = args.split(" ")
        if len(input)==1 and input[0]=="":
            return False
        return True

    def validate_add_sound(self, args):
        """Validates the add_sound command.
        """
        # TODO: implement, move validation stuff in the function to here.
        return True

    def validate_remove_sound(self, args):
        """Validates the remove_sound command.
        """
        # TODO: implement
        return True

    def validate_delay(self, args):
        """Validates the delay subcommand of play command.
        """
        # TODO: implement
        return True