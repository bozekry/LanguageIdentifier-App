<h1 style="font-size: 36px;">Language Identifier Project</h1>
<p style="font-size: 20px;">This project is a language identifier that can classify text into one of 17 languages: Arabic, Danish, Dutch, English, French, German, Greek, Hindi, Italian, Kannada, Malayalam, Portuguese, Russian, Spanish, Swedish, Tamil, and Turkish. The classifier uses a bag-of-words representation and Naive Bayes classification to make predictions. </p>

<h1 style="font-size: 36px;">Dataset</h1>

<p style="font-size: 20px;">The dataset used for this project consists of texts in the 17 different languages mentioned above. The dataset was collected from various sources, including news articles, Wikipedia pages, and social media posts.</p>

<h1 style="font-size: 36px;">Text Preprocessing</h1>

<p style="font-size: 20px;">
  Before extracting the bag-of-words representation, we used the re library to preprocess the text. Specifically, 
  we performed the following steps:
  1-Removed any non-alphabetic characters from the text, such as punctuation and numbers, using regular expressions.                                                 
  
  2-Converted all text to lowercase using the lower() function.
</p>

<h1 style="font-size: 36px;">Bag-of-words Representation</h1>


<p style="font-size: 20px;">To represent the preprocessed texts in a format that can be used for classification, we used a bag-of-words representation. In this approach, each text is represented as a vector of word frequencies, where each element in the vector corresponds to a unique word in the dataset.
  I used the scikit-learn library to implement the Bag-of-words Representation



</p>

<h1 style="font-size: 36px;">Naive Bayes Classification</h1>

<p style="font-size: 20px;">I used a Naive Bayes classifier to train a model on the bag-of-words representation of the dataset. The classifier is a probabilistic model that calculates the probability of a text belonging to each of the 17 languages, based on its bag-of-words representation.
I used the scikit-learn library to implement the Naive Bayes classifier.</p>
<h1 style="font-size: 36px;">Usage</h1>

<p style="font-size: 20px;">To use the language identifier, you can run the (streamlit run LanguageIdentifier.py) in your local machine and provide a text file as input. The script will output the predicted language for the text.</p>


<h1 style="font-size: 36px;">Conclusion</h1>
<p style="font-size: 20px;">Overall, this language identifier project demonstrates how bag-of-words representation and Naive Bayes classification can be used to classify text into multiple languages. The project also shows how the re library can be used for text preprocessing (removing non-alphabetic characters and converting text to lowercase). The project can be extended to include more languages and more advanced text processing techniques.</p>
<h1 style="font-size: 36px;">the shape of the app</h1>

![Deployment](https://github.com/bozekry/LanguageIdentifier-App/blob/main/Screenshot%20(106).png)











