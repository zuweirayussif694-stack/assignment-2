customer_name = "zuweira yussif"
clean_name = customer_name.strip()
lowercase_name = clean_name.lower()
titlecase_name = clean_name.title()
print("original name:", customer_name)
print("cleaned name:", clean_name)
print("lowercase name:",lowercase_name)
print("titlecase name:", titlecase_name)
print("lenght of name:", len(clean_name))

book_title = "the great circus in India"
formatted_title = book_title.capitalize()
print("original book title:", book_title)
print("formatted book title:", formatted_title)

product_code = "bk-345-NOVEL"
uppercase_code = product_code.upper()
new_seperator_code = uppercase_code.replace("-", "/")
print("original product code:", product_code)
print("uppercase product code:", uppercase_code)
print("new seperator product code:", new_seperator_code)


review = "This book is great. I love it!"
book_count = review.count("book")
print("review:", review)

serial_number = "4567839741"
is_digit_only =serial_number.isdigit()
print("serial number:", serial_number)
print("is serial number digit only?", is_digit_only)

url_parts = ["the", "book","nook","online"]
url_strings = "-".join(url_parts)
sentence_string = " ".join(url_parts)
print("URL string;", url_strings)
print("Sentence string:", sentence_string)

offer_code = "FREESHIPPING"
is_offer_code_uppercase = offer_code.isupper()
print("offer code:", offer_code)
print("is offer code uppercase?", is_offer_code_uppercase)

feedback_message = "I am very happy with your service."
message_lenght = len(feedback_message)
print("feedback message;", feedback_message)
print("feedback message lenght:", message_lenght)
