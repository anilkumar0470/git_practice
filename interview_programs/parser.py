import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='Your Name')
parser.add_option('-a', '--age', dest='age', help='Your Age', type=int)

(args, options) = parser.parse_args()
print (options)
print (args)