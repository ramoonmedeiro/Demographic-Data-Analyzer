import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = list(df['race'].value_counts())

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total = df['education'].value_counts().sum()
    val_bachelors = df['education'].value_counts()[2]  
    percentage_bachelors = round((val_bachelors/total)*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mask1 = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    val_high = df[mask1]['education'].value_counts().sum()
    higher_education = round((val_high/total)*100, 1)

    # low education is 100 - high education
    lower_education = 100 - higher_education

    # percentage with salary >50K

    mask2 = df['salary'] == '>50K'
    val_high_rich = df[mask1 & mask2]['salary'].value_counts().sum()
    higher_education_rich = round((val_high_rich/val_high)*100, 1)

    # lower education rich
    # not mask1 == ~mask1
    val_lower = df[~mask1]['education'].value_counts().sum()
    val_lower_rich = df[~mask1 & mask2]['salary'].value_counts().sum()
    lower_education_rich = round((val_lower_rich/val_lower)*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    total_person = df[df['hours-per-week'] == df['hours-per-week'].min()].shape[0]
    num_min_workers = df[mask2 & (df['hours-per-week'] == df['hours-per-week'].min())].shape[0]
    rich_percentage = round((num_min_workers/total_person) * 100, 0)

    # What country has the highest percentage of people that earn >50K?

    countries = list(df['native-country'].unique())
    d = {}
    for country in countries:
        total = df[df['native-country'] == country]['native-country'].shape[0]
        mask = df['native-country'] == country
        rich_people = df[mask & mask2].shape[0]
        percent = round((rich_people/total)*100, 1)
        d[country] = percent

    highest_earning_country = sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]
    highest_earning_country_percentage = sorted(d.items(), key=lambda x: x[1], reverse=True)[0][1]

    # Identify the most popular occupation for those who earn >50K in India.
    mask6 = df['native-country'] == 'India'
    top_IN_occupation = df[mask6 & mask2]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) #
        print("Average age of men:", average_age_men) #
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%") #
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
