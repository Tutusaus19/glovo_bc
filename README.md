# Business Case - CRM Tech Specialist
        This exercise is designed to showcase your marketing automation problem solving using
        technical means. It consists of a few homework tasks that can be executed in diverse ways.
        Don’t worry about delivering the perfect outcomes as your approach on identifying and
        delivering them matters as much. Please be as descriptive as you consider necessary.
        The tasks should be sent in a presentation or document format saved as .pdf file, 72 hours after
        receiving the assessment.
        Context
        CRM role is to grow users lifetime value by nudging key conversions across user lifecycle
        through marketing automation. To do so we build and adjust retention strategies, continuously
        optimizing initiatives based on data insights and tech tooling as well as overseeing new growth
        opportunities.
## Tasks

### Case 1: User Custom Attribute automation
        `` a. Files needed: CSV raw data attached.
        Please write an SQL Query that outputs the last 3 store IDS from customers who are
        from Spain, living outside Barcelona whose last order is within the last 30 days, and who
        have more than 2 orders in total.
        
        `` b. Using publicly accessible Braze documentation from here:
        https://www.braze.com/docs/api/endpoints/user_data/post_user_track/
        Write a script in python that retrieves the users from question 1 and updates their
        hypothetical profile in Braze using the above endpoint from the documentation
        (user/track). We want to update user profiles in Braze with the last 3 store IDs they
        purchased from.
        
        `` c. Bonus
        Assuming the data might get updated daily, write a script in python or describe the
        logic in a detailed way of how you would work with the data so we can avoid sending
        the same value for the attribute, but only update the attributes with changed data.

### Case 2: Restaurant images improvements
        Below you can find the image of a partner restaurant in Glovo:
        https://res.cloudinary.com/glovoapp/Stores/woeqwd5pxqel8z3p5dey
        Assuming this restaurant has an active promotion of 20% off on all catalog items and a
        rating of 91%.
        Please write a python script to combine the promotion information with the existing
        image into a new image that will display the promotion as an overlay.
        The aesthetic/design quality of the image won't be assessed but rather the functionality
        of the code.

### Case 3: Events maintenance
        The CRM Team has reported that the event add_to_cart has not been working in their
        ongoing lifecycle campaigns. The team has reached CRM Tech for support. You took over
        the case and need to provide an action plan immediately.
        Please outline the steps you would take to investigate the issue and after this list the
        stakeholders you would involve. As part of the solution please give details on how you
        would communicate with them and an example of the message (describe it individually
        if more than one stakeholder should be involved). You can also add here information
        about how you’d follow up in a few days, close the case and share a Post-Mortem.
### Case 4: Communications localisation
        Glovo is one the most popular food and groceries delivery app in Spain. Mainly their
        customers speak Spanish but often some of them speak English. Please describe below
        - and share the code snippet - how you could add liquid tags and conditional logic in
        push-notification messages to let Braze evaluate the user’s language and display the
        message in the correct language. Please feel free to add any other relevant personalized
        information retrieving data from the user profile or any other source.
        Related resources:
        https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid