# Stress-Level-Dataset-Project

Tyler deLellis & Ruiming Zeng

Student stress is an increasingly common issue that affects academic performance, mental health, and overall well-being of students. Research indicates that 60% of students report experiencing stress every day, and 1 out of 5 students are stressed most of the time. The purpose of this project is to identify the primary causes of student stress, determine which stressors have the greatest impact, and analyze patterns within psychological, academic, social, physiological, and environmental domains.

We used the Student Stress Monitoring Dataset we found on Kaggle which surveyed 843 college students on 20+ stress related features. The 5 categories surveyed were:

Psychological: anxiety, depression, self-esteem, mental health history
Physiological: breathing difficulty, headaches, blood pressure, sleep quality
Environmental: basic needs, safety, living conditions, noise level
Academic: academic performance, study load, teacher relationships, career concerns
Social: peer pressure, social support, extracurricular activities, bullying

The analysis of this dataset included 3 main steps. First, we wanted to see the average stress score. We calculated the mean score for each stressor to identify chronic, long-term sources of stress. We also measured which stressors triggered the highest response rate. Our dataset was graded 1-5 so we wanted to see what specific stressors had the most 5's. Lastly, for each of the 5 tested categories, we identified the highest scoring stressor. Additionally, we made scatterplots for each category so we can see how diverse the surveys were for every category. When going over the data, the csv file was pretty clean so no data cleaning was needed.

This analysis was performed in Python using pandas and matplotlib.

1. Average Stress Scores

<img width="876" height="509" alt="image" src="https://github.com/user-attachments/assets/3ee69283-2957-44c6-bb8c-a3c4ee6461d4" />

The average stress analysis showed that self-esteem was the highest overall stressor, followed closely with depression and anxiety. These results show that psychological pressures have the strongest impact on students, while academic demands and unmet basic needs also contribute to daily stress.

2. Top Stressor in Each Category

<img width="884" height="825" alt="image" src="https://github.com/user-attachments/assets/cf53c75e-70e0-4626-90d3-b4d38a4c8c10" />

Each stress category had its own leading factor. Self-esteem was the strongest psychological stressor, while stress-related breathing difficulty was the top physiological one. Basic needs ranked highest in the environmental category, academic performance dominated the academic portion of the survey, and extracurricular activities were the top social stressor. These results show student stress emerges from multiple areas of their lives.

3. Maximum Stress Level (Score = 5)

<img width="872" height="576" alt="image" src="https://github.com/user-attachments/assets/5a268da6-a5a9-4d72-a458-1fdef9b9136d" />

When looking at the most severe stress ratings, sleep quality received the highest number of level 5 responses, making it the most intense stressor for students. Basic needs and future career concerns also scored high, showing that environmental stability and academic unpredictability are major triggers of stress.

4. Combined Top Stressors

<img width="660" height="743" alt="image" src="https://github.com/user-attachments/assets/f36d046f-450e-467a-b650-ff206395d8ba" />

Combining both average scores and severe stress responses, the overall top stressors were self-esteem, depression, anxiety, sleep quality, and future career concerns. Together, these highlight the strong influence of psychological well-being, sleep health, and academic expectations on student stress.

Additionally, we wanted to see how the voting was for each category, so we generated scatterplots to compare how students ranked each stressor.

<img width="640" height="424" alt="image" src="https://github.com/user-attachments/assets/d3f065d6-58cd-4fda-9628-d9617f3d26eb" />
<img width="640" height="424" alt="image" src="https://github.com/user-attachments/assets/4852132b-6a02-43bf-b89e-6a5b16605857" />
<img width="640" height="424" alt="image" src="https://github.com/user-attachments/assets/48edef89-f34d-4c8e-88b4-c3384c05357b" />
<img width="634" height="424" alt="image" src="https://github.com/user-attachments/assets/1ddff291-37df-46ba-bdb7-c20929efbbb2" />
<img width="640" height="424" alt="image" src="https://github.com/user-attachments/assets/0f498f69-605a-4fa4-99e5-7047ab128bf1" />
These scatterplots show a closer look at how the students rated each stressor on the 1-5 scale. Because each point represents an individual student's vote, the density and spread of the dots reveal how different the opinions between the students were. Stressors with thicker, denser clusters indicate areas where many students consistently reported stress, while thinner clusters suggested more varied experiences among the surveyed students.


Overall, our analysis shows that student stress is shaped by a combination of many different factors. Psychological stressors such as self-esteem, depression, and anxiety were the most influential, while issues like sleep quality and career concerns created the most intense spikes in stress. Together, these findings highlight the importance of supporting students’ mental health, providing academic guidance when necessary, and improving access to basic needs and stable living conditions on campus.
