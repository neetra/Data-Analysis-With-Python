import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # Remove trailing whitespace characters from columns names
    df.columns = df.columns.str.strip()
   

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?

    # Filter to only men
    men = df[df['sex'] == 'Male']  # adjust the column name & value if needed

    # Compute average age
    average_age_men = round(men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_count = len(df)
    bachelors_count = (df['education'] == 'Bachelors').sum()
    percentage_bachelors = round((bachelors_count / total_count) * 100, 1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # Define which educations count as "advanced"
    advanced = ["Bachelors", "Masters", "Doctorate"]

    # Filter to people with advanced education
    higher_edu = df[df["education"].isin(advanced)]

    # Count how many of them make >50K
    higher_edu_rich = higher_edu[higher_edu["salary"] == ">50K"]

    # Compute percentage
    higher_education_rich = round((len(higher_edu_rich) / len(higher_edu)) * 100,1)
    # Filter people without advanced education
    no_advanced = df[~df["education"].isin(advanced)]

    # Among them, find those making >50K (assuming income column values are like '>50K')
    no_advanced_rich = no_advanced[no_advanced["salary"] == ">50K"]

    # Calculate percentage
    lower_education_rich = round((len(no_advanced_rich) / len(no_advanced)) * 100, 1)    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours =  df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
# Step 2: Filter the people who work minimum hours
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    # Step 3: Calculate the percentage of those who earn >50K
    rich_percentage = (num_min_workers[num_min_workers["salary"] == ">50K"].shape[0] / 
                   num_min_workers.shape[0]) * 100
        
    # What country has the highest percentage of people that earn >50K?

    percent = df[df["salary"] == ">50K"].groupby("native-country").size() / df.groupby("native-country").size() * 100

    # Get the country with the highest percentage
    highest_earning_country = percent.idxmax()
    highest_earning_country_percentage = round(percent.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    # Filter for people from India who earn >50K
    india_rich = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    # Find the most common occupation
    top_IN_occupation = india_rich["occupation"].mode()[0]
   
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
