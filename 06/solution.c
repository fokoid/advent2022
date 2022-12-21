#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* data;
    size_t index;
    size_t length;
    // keep count of characters in ringbuffer, makes rbIsUnique run in O(L) rather than O(N^2)
    // where L - alphabet size, N - ring buffer size
    int* cache;
} RingBuffer;

void rbAlloc(RingBuffer* rb, size_t length) {
    rb->index = 0;
    rb->length = length;
    rb->data = malloc(length * sizeof(int));
    rb->cache = malloc(26 * sizeof(int));
    for (size_t i = 0; i < 26; ++i) {
        rb->cache[i] = 0;
    }
}

int rbIsFull(RingBuffer* rb) {
    return rb->index >= rb->length;
}

int rbIsUnique(RingBuffer* rb) {
    if (!rbIsFull(rb)) {
        return 0;
    }
    for (int i = 0; i < rb->length; ++i) {
        for (int j = i + 1; j < rb->length; ++j) {
            if (rb->data[i] == rb->data[j]) {
                return 0;
            }
        }
    }
    return 1;
}

int rbIsUniqueCache(RingBuffer* rb) {
    if (!rbIsFull(rb)) {
        return 0;
    }
    for (int i = 0; i < 26; ++i) {
        if (rb->cache[i] > 1) {
            return 0;
        }
    }
    return 1;
}

void addCache(RingBuffer* rb, int value) {
    ++rb->cache[value - 'a'];
}

void delCache(RingBuffer* rb, int value) {
    int index = value - 'a';
    int cacheValue = rb->cache[index];
    rb->cache[index] = cacheValue > 0 ? cacheValue - 1 : 0;
}

void rbInsert(RingBuffer* rb, int value) {
    if (rbIsFull(rb)) {
        delCache(rb, rb->data[rb->index % rb->length]);
    }
    rb->data[rb->index++ % rb->length] = value;
    addCache(rb, value);
}

void rbFree(RingBuffer* rb) {
    if (rb->length != 0) {
        free(rb->data);
        free(rb->cache);
        rb->data = NULL;
        rb->length = 0;
    }
}

void rbPrint(RingBuffer* rb) {
    for (size_t i = 0; i < rb->length; ++i) {
        printf("%d ", rb->data[i]);
    }
    printf("\n");
}

int main(void) {
    int solution1 = -1, solution2 = -1;
    RingBuffer rb1;
    RingBuffer rb2;

    rbAlloc(&rb1, 4);
    rbAlloc(&rb2, 14);
    FILE* file = fopen("input.txt", "r");

    int c;
    while ((c = fgetc(file)) != EOF && (solution1 == -1 || solution2 == -1)) {
        rbInsert(&rb1, c);
        rbInsert(&rb2, c);
        if (solution1 == -1 && rbIsUniqueCache(&rb1)) {
            solution1 = rb1.index;
        }
        if (solution2 == -1 && rbIsUniqueCache(&rb2)) {
            solution2 = rb2.index;
        }
    }

    fclose(file);
    rbFree(&rb1);
    rbFree(&rb2);

    printf("Part 1: %i\n", solution1);
    printf("Part 2: %i\n", solution2);
    return 0;
}