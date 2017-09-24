# the methods in the namespace
from autonomio.commands._wrapper import train
from autonomio.commands._wrapper import hyperscan
from autonomio.commands._wrapper import wrangler
from autonomio.commands._wrapper import data
from autonomio.commands._wrapper import predictor

# stuff we don't want in the namespace
try:
	del models
except NameError:
	pass

try:
	del datetime
except NameError:
	pass

try:
	del commands
except NameError:
	pass

try:
	del text.ngrams
except NameError:
	pass

try:
	del plots.lstm_plots
except NameError:
	pass

try:
	del plots.plots
except NameError:
	pass

try:
	del plots.trainplot
except NameError:
	pass

try:
	del transforms.math
except NameError:
	pass

try:
	del text.ascify
except NameError:
	pass

try:
	del text.processing
except NameError:
	pass

try:
	del text.recognition
except NameError:
	pass

try:
	del transforms.onehot_encoding
except NameError:
	pass

try:
	del text.cleaning
except NameError:
	pass

try:
	del text.stopwords
except NameError:
	pass

__version__ = "0.5.0"
