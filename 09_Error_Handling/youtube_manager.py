# while true is for the taking the input from the user

# the match choice is good for the selecting the choice of the case

# def main() is the special method is used for making the code friendly and after the main you have to use indentation ctrl + ] you ave to use after the main after the main indentation all code is part of main

# json.load(file) will go to the file and load the data of the file and also make it to the json or string format data into json
# json.dump will help to write the what you want
# enumerate (videos, start=1) will help you to start the indexing with the one because it starts form the zero




import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type (test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)
    

def list_all_videos(videos):
     print("\n")
     print("*" * 70)
     for index, video in enumerate(videos,start= 1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def Update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1<=index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid video index slected")



def main():
 videos = load_data()
 while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube video ")
        print("2. Add a youtube video")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                Update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            # this break is used for the exit of the app. By the way if someone is used the other case instead of case mentioned then
            case _:
                print("Invalid Choice")
if __name__ == "__main__":
    main()



    

    







