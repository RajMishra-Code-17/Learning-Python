# first we have implemented the or import the sqlite3 and after that i have used a variable conn to connect the sqlite3 to the youtube_videos.db
# we can take the string into the triple (''' ''') and its formating will be saved so we can use the triple court
# if the name of the function is main then execute the main and we have made a while loop and its value is true so the loop dont break
# by the conn.close() we have closed the loop
# after the execute of the cursor you can commit the cursor



import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()      # <-- add ()

cursor.execute("""
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
""")


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)



def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (? , ?)", (name, time))
    conn.commit()



def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE id = ?", (new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE from the videos where id id = ?",(video_id,))
    conn.commit()

def main ():
    while True:
        print("\n Youtube manger app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")


        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()