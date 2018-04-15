import os, sys, time, math

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

def loadContents(filename):
	print 'Loading file {}, size is {} bytes'.format(filename, os.path.getsize(filename))
	contents = []
	nlines = 0
	with open(filename, 'r') as f:
		for line in f:
			nlines += 1
			words = line.split()
			contents.extend(words)
	return (contents, nlines)

if __name__ == '__main__':
	filename = sys.argv[1]

	contents, nlines = measureTime(loadContents)(filename)
	print 'file has {} words in {} lines'.format(len(contents), nlines)
	
	counts = {}
	starttime = time.time()
	for word in contents:
		word = word.lower()
		if not (word in counts):
			counts[word] = 0
		counts[word] += 1
	takentime = time.time() - starttime
	print 'words counted in {} sec'.format(roundToDecimals(takentime, 3))

	starttime = time.time()
	countofwords = [(count, word) for word,count in counts.iteritems()]
	sortedcounts = sorted(countofwords, reverse=True)
	takentime = time.time() - starttime
	print 'word counts sorted in {} sec'.format(roundToDecimals(takentime, 3))

	for i in xrange(20):
		current = sortedcounts[i]
		print '#{}: {} ({}, {}%)'.format(i+1, current[1], current[0], roundToDecimals(current[0]/float(len(contents))*100.0, 3))
