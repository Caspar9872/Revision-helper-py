dict = {
"acid_1":"tea",
"acid_2":"yoghurt",
"acid_3":"vinegar",
"acid_4":"grape",
"acid_5":"apples",
"acid_6":"citrus fruits",
"acid_7":"soft drinks",
"acid_8":"spinach",
"acid_9":"body lotion",
"acid_10":"hair conditioner",
"acid_11":"toilet cleaner",
"acid_12":"aspirin",
"alkali_1":"toothpaste",
"alkali_2":"glass cleaner",
"alkali_3":"kitchen cleaner",
"alkali_4":"drain cleaner",
"alkali_5":"soap",
"alkali_6":"alkaline batteries"
}
import revisionHelper as rh
rh.ask_questions(dict,shuffle=False)  # Ask the user questions based on the dictionary