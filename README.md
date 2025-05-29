# Image Quiz Game

## Overview

The **Image Quiz Game** is a web-based application built using the Flask framework in Python. The game challenges players to identify images by their names within a set time frame. It is designed to be both fun and educational, making it suitable for various age groups and purposes, such as team-building exercises, educational tools, or simply as a casual game.

The application features a user-friendly interface, dynamic question generation, and detailed logging of player performance. It also includes a manipulation feature that allows specific players to receive custom sets of questions, adding an extra layer of personalization.

---

## Features

### 1. **Dynamic Question Generation**
   - The game randomly selects a set of images from a predefined folder (`pic`) to serve as questions.
   - The number of questions can be configured via the `NUMBER_OF_QUESTIONS` variable.
   - Specific players can receive custom sets of questions using the `MANIPULATE` dictionary.

### 2. **User Authentication and Session Management**
   - Players enter their usernames to start the game.
   - Session management ensures that each player's progress, score, and log data are tracked throughout the game.

### 3. **Real-Time Feedback**
   - Players receive immediate feedback on their answers, including whether they were correct and a clue image to help them learn.

### 4. **Detailed Logging**
   - The game logs each player's performance, including:
     - The image shown.
     - The correct answer.
     - The player's answer.
     - The time taken to answer.
     - Whether the answer was correct.
   - Logs are saved in the `logs` folder for later review.

### 5. **Customizable Player Lists**
   - The game supports predefined lists of players and names, which can be customized via `Players.txt` and `names.txt`.

### 6. **Responsive Design**
   - The game is designed to be responsive and works seamlessly across different devices.

---

## Installation and Setup

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)

### Steps to Run the Application
1. **Clone the Repository**
   ```bash
   git clone https://github.com/b31556/RecognitionGame
   cd RecognitionGame
   ```

2. **Set Up the Environment**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install flask
     ```

3. **Prepare the Image Folder**
   - Place your images in the `pic` folder. Ensure the filenames are descriptive, as they will serve as the correct answers.

4. **Prepare Player Lists**
   - Create `Players.txt` and `names.txt` files in the root directory. Each file should contain one entry per line.

5. **Run the Application**
   ```bash
   python app.py
   ```
   The application will be available at `http://0.0.0.0:5000`.

---

## Usage

### 1. **Home Page**
   - Players enter their usernames on the home page to start the game.

   ![Home Page](screenshots/home.png) <!-- Add a screenshot here -->

### 2. **Game Interface**
   - Players are presented with an image and a text box to enter their answer.
   - The interface displays the current question number and provides a clue image after each answer.

   ![Game Interface](screenshots/game.png) <!-- Add a screenshot here -->

### 3. **Results Page**
   - After completing all questions, players are shown their score and a detailed breakdown of their performance.

   ![Results Page](screenshots/results.png) <!-- Add a screenshot here -->

---

## Customization

### 1. **Manipulating Questions for Specific Players**
   - To customize questions for specific players, modify the `MANIPULATE` dictionary in the code:
     ```python
     MANIPULATE = {
         "Player Name": ["image1.png", "image2.png", "image3.png"]
     }
     ```

### 2. **Changing the Number of Questions**
   - Update the `NUMBER_OF_QUESTIONS` variable to set the number of questions per game.

### 3. **Adding or Removing Players**
   - Edit the `Players.txt` and `names.txt` files to update the list of players and names.

---

## Logs and Analytics

The application generates detailed logs for each game session, stored in the `logs` folder. These logs can be used for:
- Tracking player performance over time.
- Identifying common mistakes or challenging questions.
- Analyzing response times and accuracy.

Example log entry:
```
Player: JohnDoe
Total score: 7/10
Details:
Question 1: Image: cat.png, Correct: cat, Your answer: dog, Time: 5.32s, Correct: No
Question 2: Image: tree.png, Correct: tree, Your answer: tree, Time: 3.12s, Correct: Yes
...
```

---

## Future Enhancements

1. **Multiplayer Mode**
   - Allow multiple players to compete in real-time.

2. **Leaderboard**
   - Add a leaderboard to display top scores.

3. **Advanced Analytics**
   - Provide visual analytics (e.g., graphs) for player performance.

4. **Mobile App Integration**
   - Develop a mobile app version for easier access.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

Ez a projekt a módosított GNU General Public License (GPL) v3 licenc alatt áll. A licenc teljes szövege megtalálható a LICENSE fájlban.

Fontos: Ha módosítod a programot, köteles vagy a módosított változatot nyilvánosan hozzáférhetővé tenni, a módosított GPL licenc 5(e) szakaszában foglaltak szerint.

---

## Acknowledgments

- Thanks to the Flask community for providing an excellent framework.
- Special thanks to all contributors and testers.

---

## Screenshots

<!-- Add more screenshots here -->
![Game Interface](screenshots/game.png)
![Results Page](screenshots/results.png)

---

Enjoy playing the **Image Quiz Game**! For any questions or feedback, please open an issue or contact the maintainers.
