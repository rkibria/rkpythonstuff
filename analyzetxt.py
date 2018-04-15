import os, sys, time, math, string, argparse

def roundToDecimals(num, decs):
	factor = math.pow(10.0, decs)
	return math.trunc(num * factor)/factor

def measureTime(func):
	def measuretimeWrapper(*args, **kwargs):
		starttime = time.time()
		result = func(*args, **kwargs)
		takentime = time.time() - starttime
		print '* took {} sec'.format(roundToDecimals(takentime, 3))
		return result
	return measuretimeWrapper

@measureTime
def loadContents(filename):
	print 'Loading file {}, size is {} bytes'.format(filename, os.path.getsize(filename))
	contents = []
	nlines = 0
	with open(filename, 'r') as f:
		for line in f:
			nlines += 1
			words = line.split()
			contents.extend(words)
	print 'Found {} words in {} lines'.format(len(contents), nlines)
	return (contents, nlines)

@measureTime
def countWords(contents):
	print "Count words"
	counts = {}
	for word in contents:
		word = word.lower()
		word = word.translate(None, string.punctuation)
		if not (word in counts):
			counts[word] = 0
		counts[word] += 1
	return counts

@measureTime
def sortCounts(counts):
	print "Sorting by count"
	countofwords = [(count, word) for word,count in counts.iteritems()]
	sortedcounts = sorted(countofwords, reverse=True)
	return sortedcounts

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("filename", help="path to text file")
	args = parser.parse_args()

	contents, nlines = loadContents(args.filename)
	counts = countWords(contents)
	sortedcounts = sortCounts(counts)

	for i in xrange(200):
		current = sortedcounts[i]
		print '#{}: {} ({}, {}%)'.format(i+1, current[1], current[0], roundToDecimals(current[0]/float(len(contents))*100.0, 3))
