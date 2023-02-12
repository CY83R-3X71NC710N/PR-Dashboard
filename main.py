import csv
import requests

def get_pull_requests(repo):
    pull_requests = []
    page = 1
    while True:
        response = requests.get(f'https://api.github.com/repos/{repo}/pulls?page={page}')
        data = response.json()
        if not data:
            break
        pull_requests.extend(data)
        page += 1
    return pull_requests

def get_pull_request_data(pull_request):
    pr_number = pull_request['number']
    date_opened = pull_request['created_at']
    date_closed = pull_request['closed_at']
    user_opened = pull_request['user']['login']
    user_closed = pull_request['closed_by']['login'] if pull_request['closed_by'] else None
    status = pull_request['state']
    comments = pull_request['comments']
    files_changed = pull_request['changed_files']
    return (pr_number, date_opened, date_closed, user_opened, user_closed, status, comments, files_changed)

def main():
    repo = input("Enter the name of the GitHub repository (e.g. user/repo): ")
    filename = input("Enter the name of the CSV file: ")
    pull_requests = get_pull_requests(repo)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PR Number', 'Date Opened', 'Date Closed', 'User Opened', 'User Closed', 'Status', 'Number of Comments', 'Number of Files Changed'])
        for pull_request in pull_requests:
            pr_data = get_pull_request_data(pull_request)
            writer.writerow(pr_data)
    print(f"Data from pull requests in repository {repo} has been saved to {filename}.")

if __name__ == "__main__":
    main()
