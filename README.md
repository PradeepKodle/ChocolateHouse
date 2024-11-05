
# Chocolate House Management System

## Overview
A Python application using SQLite to manage:
- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

## Setup

### Prerequisites
- Docker

### Running the Application
1. Clone the repository.
2. Run the following commands to build and start the app in Docker:
   ```bash
   docker build -t chocolate-house .
   docker run -it --rm chocolate-house
   ```

## Functionality
- **Add Seasonal Flavor**: Record seasonal flavors and availability dates.
- **Add Ingredient**: Track ingredient name and quantity.
- **Customer Suggestions**: Log customer suggestions and allergy concerns.

## Edge Cases and Validations
- **Ingredient Quantity**: Ensures quantity is an integer.
- **Date Format**: Ensures dates are in `YYYY-MM-DD`.
- **Empty Fields**: Prevents empty strings in flavor and ingredient names.

## Testing Steps
1. **Seasonal Flavor Addition**:
   - Add a seasonal flavor and validate it appears in the database.
2. **Inventory Addition**:
   - Add ingredients with quantities and ensure they’re saved.
3. **Customer Suggestion**:
   - Add a suggestion, and verify it’s logged.
