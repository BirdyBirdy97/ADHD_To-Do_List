from glob import glob
from phrases import congrats_phrases
import random

current = ""

class TaskCreator:


	# # # # # # # # # # # # # # # # # # Setup # # # # # # # # # # # # # # # # # # 


	def __init__(self):
		self.to_do_tasks = ["hello", "how", "are", "you"]
		self.completed_tasks = ["done"]

	def ask_input(self):
		"""Gets input for self.to_do_tasks."""
		list_of_tasks = input("What do you need to do today? Please separate the tasks with the enter key.\n\n")
		self.to_do_tasks = list_of_tasks.split("enter")

	def again(self):
		"""Determines based on input whether or not ask_input should run again."""
		another = input("Do you have another item? Y/N\n").lower()
		if another == "y":
			return True
		elif another == "n":
			return False
		else:
			print("Invalid input.")
			self.again()


	# # # # # # # # # # # # # # # # # # Button functions # # # # # # # # # # # # # # # # # #


	def current_task(self):
		"""Reassigns the value for self.current."""
		current = random.choice(self.to_do_tasks)
		return current

	def skip(self):
		"""Skips the current task for now but it stays in self.to_do_tasks."""
		self.current_task()

	def finished(self):
		"""Moves the completed task into self.completed_tasks and removes it from self.to_do_tasks so it can't be posted again."""
		self.completed_tasks.append(current)
		self.to_do_tasks.remove(current)
		self.congrats_phrase()

	def n_a_today(self):
		"""Removes the current task from self.to_do_today without removing it from the saved list"""
		self.to_do_tasks.remove(current)


	# # # # # # # # # # # # # # # # # # End Behaviours # # # # # # # # # # # # # # # # # #


	def done_for_day(self):
		"""Lets program know when the end of day routine should be run."""
		if len(self.to_do_tasks) == 0:
			return True
	
	def end_of_day_routine(self):
		"""Prints an end statement with the number of finished tasks"""
		num_of_tasks_completed = len(self.completed_tasks)
		return f"Amazing work! You've completed {num_of_tasks_completed} tasks today!\nHere's everything you've done:"
		
	def print_comp_list(self):
		"""Prints out the completed_tasks list as a vertical split list"""
		for task in self.completed_tasks:
			return task


	# # # # # # # # # # # # # # # # # # Misc Commands # # # # # # # # # # # # # # # # # # 


	def congrats_phrase(self):
		"""Selects one of the motivational phrases"""
		current_congrats_phrase = random.choice(congrats_phrases)
		return current_congrats_phrase
