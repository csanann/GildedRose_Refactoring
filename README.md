# GlidedRose Refactoring

This project is a refactoring exercise based on the Gilded Rose Refactoring Kata. the goal is to improve the existing codebase for managing the inventory of a small inn, where the quality of items changed over time.

## Problem Statement

The Gilded Rose inn sells various items, each with its own set of quality management rules. The challenges is to update the existing inventory management system to accommodate new item types and ensure that the quality of items is correctly updated according to their specific rules.

## Approach

The problem was approached using principles of Object-Oriented Programming (OOP) and Test-Driven Development(TDD). The following steps were followed:
1. Identify unique Item Behavior: 
The existing item types were analyzed to identify their unique behaviors and quality update rules. This included understanding how each item's quality changes over time and any special conditions that apply.
2. Specific Item Classes:
Separate classes were created for each item type to encapsulate their unique behavior and manage the quality update process. This approach simplifies the code, improve readability, and allows for easier maintenance and future expansion.
3. Test-Driven Development:
Comprehensive tests were written for each item class to verify the correctness of the implementation. These tests ensure that the code behaves as expected and enables safer modifications in the future.
4. Edge Case Handling:
Edge cases, such as the lower and upper bounds for item quality, were considered and handled within eac item class. This ensures that the quality of items never goes below 0 or above 50 (expect for the special item "Sulfuras").

## Installation and Setup

To run the Gilded Rose Refactoring project locally, follow these steps:
1. Clone the repository to your local machine.
2. Make sure you have Python( version 3.7 or higher)installed.
3. Install the project dependencies by running 'pip install -r requirements.txt'.

## Running the Tests

To execute the test suite and validate the implementation, run the following command:
'''
pytest tests/

'''
This command will run all the unit tests for item classes and provide feedback on the code's correctness and coverage.

## Code Structure

The project's code is organized as follows:
'''
- 'src/': contains the source code for the item classes (aged_brie_item, backstage_passes_item files)
- 'tests/': includes the unit tests for the item classes as well the integration test for the GildedRose class (integration_test_gilded_rose file)
- 'pytest.ini': configuration file for pytest.
- README.md': provides and overview of the project and instructions for running the code.

## Assumptions and Limitations

during the refactoring process, the following assumptions were made:
- The existing item class 'Item' should not be modified, as it belongs to external code.
- The focus of the refactoring was on improving the code structure and introducing separate item classes for better encapsulation and maintainability.
- The requirements for item behavior and quality management were based on the original problem statement.

## Further Improvements

Here are some potential areas for further improvement or expansion:
- Enhancing test coverage for edge cases and additional scenarios.
- Implementing a more comprehensive logging or reporting mechanism to track item updates and changes.
- Integrating the code into a larger inventory management system with database persistence.

There improvements can be explored based on the specific needs and requirements of the project.
