# API Request GitLab

This repository contains a Python script that demonstrates how to make API requests to the GitLab API and retrieve information about projects. It utilizes the requests library to send HTTP requests and retrieve data in JSON format.

## How to Use

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/Api-Request-GitLab.git
   ```

2. Navigate to the project directory:

   ```
   cd Api-Request-GitLab
   ```

3. Make sure you have Python installed on your machine. If not, you can download and install Python from the official website: [python.org](https://www.python.org/).

4. Install the requests library by running the following command:

   ```
   pip install requests
   ```

5. Open the `api_request.py` file in a text editor.

6. Replace `nanuchi` in the URL `https://gitlab.com/api/v4/users/nanuchi/projects` with your GitLab username.

7. Save the file.

8. Run the script by executing the following command:

   ```
   python api_request.py
   ```

9. The script will send a GET request to the GitLab API and retrieve information about your projects.

10. The project names and their corresponding URLs will be printed to the console.

## Example

```plaintext
{
    "id": 12345678,
    "name": "My Project",
    "web_url": "https://gitlab.com/your-username/my-project"
}

Project Name: My Project
Project URL: https://gitlab.com/your-username/my-project
```

## Customization

You can customize the script to retrieve additional information or perform different API requests. The current script demonstrates how to retrieve project names and URLs, but you can explore the GitLab API documentation for more available endpoints and data.

## Contributions

Contributions to this project are welcome. If you find any issues or want to suggest improvements, please open an issue or submit a pull request.

Happy API requesting with GitLab!
