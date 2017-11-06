'''
Created on Oct 12, 2017
@author: John Nguyen
'''
import os
import PyPDF2

input_directory = "/Users/NguyenJ.MININT-3LV3JTL/InputTestCaseInPDFFormat"
output_text_file = "/Users/NguyenJ.MININT-3LV3JTL/TestCaseFromPDFToTextOutput/OutputTextFile"

os.chdir(input_directory)
set_of_all_PDF_input_files = os.listdir()

with open(output_text_file, 'a') as output_text_file:
    output_text_file.write("step number | Name | Step | Result | Testdata | ExternalId | Description \n")
    for each_PDF_input_file in set_of_all_PDF_input_files:
        step_counter = 0
        with open(each_PDF_input_file, 'rb') as PDF_input_file:
            pdfreader = PyPDF2.PdfFileReader(PDF_input_file) 
            for each_page in range(pdfreader.getNumPages()):
                set_of_test_steps = pdfreader.getPage(each_page).extractText()
                """ Get the test case ID and the external ID """
                if(each_page == 0):
                    test_case_ID, test_step_description, input_data, expected_result, external_ID, description = set_of_test_steps[0].split('|')
                    test_case_ID_holder = test_case_ID.lstrip().rstrip()
                    external_ID_holder = external_ID.lstrip().rstrip()
                      
                """ Format the test steps and write them to the output file """  
                
                for each_test_step in set_of_test_steps:
                    test_case_ID, \
                    test_step_description, \
                    input_data, expected_result, \
                    external_ID, \
                    description = each_test_step.split('|')
                    description = 'Dummny Description'
                    step_counter += 1
                    #test_step = f'{step_counter} | {test_case_ID_holder} | {test_step_description} | {input_data} | {expected_result} | {external_ID_holder}'
                    test_step = str(step_counter) + "|" + \
                                test_case_ID_holder + "|" + \
                                test_step_description.lstrip().rstrip() + "|" + \
                                expected_result.lstrip().rstrip() + "|" + \
                                input_data + "|" + \
                                external_ID_holder + "|" + \
                                description
                    print(test_step)
                    print("========================================================================")
                    output_text_file.write(test_step + "\n")
