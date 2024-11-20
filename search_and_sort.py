from flask import Flask, request, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def binary_search(video_titles, target):             # Binary search function to search for the target video title in the sorted list
    left, right = 0, len(video_titles) - 1
    while left <= right:
        mid = (left + right) // 2
        if video_titles[mid] == target:
            return mid
        elif video_titles[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def merge_sort(video_titles):                   # Merge sort function to sort the list of video titles
    if len(video_titles) > 1:
        mid = len(video_titles) // 2
        left_half = video_titles[:mid]
        right_half = video_titles[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                video_titles[k] = left_half[i]
                i += 1
            else:
                video_titles[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            video_titles[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            video_titles[k] = right_half[j]
            j += 1
            k += 1
    return video_titles

@app.route('/search', methods=['GET'])  # http://127.0.0:5000/search?title=The%20Art%20%20of%20Coding example format for query
def search_video():
    query = request.args.get('title')
    if not query:
        return jsonify({"error": "No search query provided"}), 400
    
    index = binary_search(video_titles, query)
    if index != -1:
        return jsonify({"title": video_titles[index]}), 200
    else:
        return jsonify({"error": "Video not found"}), 404

@app.route('/sort', methods=['GET']) # http://127.0.0:5000/sort example format for query
def sort_videos():
    sorted_videos = merge_sort(video_titles.copy())
    return jsonify({"sorted_videos": sorted_videos}), 200

if __name__ == '__main__':
    app.run(debug=True)