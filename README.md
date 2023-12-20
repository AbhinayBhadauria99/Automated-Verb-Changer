The project is a Python program that converts a list of English verbs into their past tense and present continuous forms. 
It handles both regular and irregular verbs using a dictionary for irregular forms and simple rules for regular forms. 
The main function demonstrates the conversion for a predefined list of verbs. The program can be customized by modifying the list of verbs and adding more irregular forms to the dictionary.
Here's an explanation of the key components of the project:



convert_verb function:

This function takes a single verb as an argument.
It checks whether the verb is irregular by looking it up in the irregular_verbs dictionary.
If the verb is irregular, it retrieves its past tense and present continuous forms from the dictionary.
If the verb is regular, it determines the past tense and present continuous forms based on simple rules (e.g., adding 'ed' or 'ing' to the verb).
The function returns a tuple containing the past tense and present continuous forms.


main function:
This function serves as the entry point of the program.
It defines a list of verbs (verbs) that need to be converted.
It iterates through the list of verbs, calling the convert_verb function for each verb, and prints the results.
irregular_verbs dictionary:

This dictionary stores irregular verbs as keys and their corresponding past tense and present continuous forms as values.
Irregular verbs have unique forms that don't follow the regular rules for forming past tense and present continuous.


Execution:
The program demonstrates how to use the convert_verb function by applying it to a predefined list of verbs.
It prints the original verb, its past tense, and its present continuous form for each verb in the list.
Customization:

You can customize the list of verbs in the main function based on your requirements.
Additional irregular verbs can be added to the irregular_verbs dictionary as needed.
