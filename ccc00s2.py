import sys
input = sys.stdin.readline

streams = []
numStreams = int(input())
for i in range(numStreams):
    x = int(input())
    streams.append(x)
while True:
    command = int(input())
    if command == 99:
        streamToSplit = int(input())
        percentageLeft = int(input())
        streams[streamToSplit - 1] *= percentageLeft / 100
        streams.insert(streamToSplit, streams[streamToSplit - 1] * 100 / percentageLeft * (100 - percentageLeft) / 100)
    elif command == 88:
        mergeStream = int(input())
        streams[mergeStream - 1] += streams[mergeStream]
        streams.pop(mergeStream)
    elif command == 77:
        break
for i in range(len(streams)):
    streams[i] = str(round(streams[i]))
print(" ".join(streams))
