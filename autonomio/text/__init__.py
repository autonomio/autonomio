from vectorize_text import vectorize_text
from recognition import part_of_speech
from recognition import entity_recognition
from processing import text_to_words
from processing import text_to_blob
from processing import word_filtering
from ascify import Ascify
from index_builder import index_builder
from processing import text_to_chars
from words_to_ints import words_to_ints
from words_to_ints import sequence_padding
from cleaning import remove_punctuation
from cleaning import remove_stopwords
from ngrams import embeds_ngrams
from ngrams import text_to_ngram

__version__ = "0.5.0"
