DATABASE_URL = 'postgres:///gotissuestest'

full_issue = {
  "url": "https://api.github.com/repos/codeforamerica/gotissues/issues/8",
  "labels_url": "https://api.github.com/repos/codeforamerica/gotissues/issues/8/labels{/name}",
  "comments_url": "https://api.github.com/repos/codeforamerica/gotissues/issues/8/comments",
  "events_url": "https://api.github.com/repos/codeforamerica/gotissues/issues/8/events",
  "html_url": "https://github.com/codeforamerica/gotissues/issues/8",
  "id": 87136867,
  "number": 8,
  "title": "Pull in data from GitHub about the clicked issues",
  "user": {
    "login": "ondrae",
    "id": 595778,
    "avatar_url": "https://avatars.githubusercontent.com/u/595778?v=3",
    "gravatar_id": "",
    "url": "https://api.github.com/users/ondrae",
    "html_url": "https://github.com/ondrae",
    "followers_url": "https://api.github.com/users/ondrae/followers",
    "following_url": "https://api.github.com/users/ondrae/following{/other_user}",
    "gists_url": "https://api.github.com/users/ondrae/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/ondrae/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/ondrae/subscriptions",
    "organizations_url": "https://api.github.com/users/ondrae/orgs",
    "repos_url": "https://api.github.com/users/ondrae/repos",
    "events_url": "https://api.github.com/users/ondrae/events{/privacy}",
    "received_events_url": "https://api.github.com/users/ondrae/received_events",
    "type": "User",
    "site_admin": "false"
  },
  "labels": [
    {
      "url": "https://api.github.com/repos/codeforamerica/gotissues/labels/enhancement",
      "name": "enhancement",
      "color": "84b6eb"
    }
  ],
  "state": "closed",
  "locked": "false",
  "assignee": "null",
  "milestone": "null",
  "comments": 1,
  "created_at": "2015-06-10T23:03:05Z",
  "updated_at": "2015-06-23T00:43:27Z",
  "closed_at": "2015-06-23T00:43:26Z",
  "body": "TEST BODY",
  "closed_by": {
    "login": "ondrae",
    "id": 595778
  },
  "clicks" : 10000000
}

trimmed_issue = {
  "html_url": "https://github.com/codeforamerica/gotissues/issues/8",
  "id": 87136867,
  "title": "Pull in data from GitHub about the clicked issues",
  "labels": [
    { "url": "https://api.github.com/repos/codeforamerica/gotissues/labels/enhancement",
      "name": "enhancement",
      "color": "84b6eb"
    }
  ],
  "state": "closed",
  "comments": 1,
  "created_at": "2015-06-10T23:03:05Z",
  "closed_at": "2015-06-23T00:43:26Z",
  "body": "TEST BODY",
  "closed_by": {
    "login": "ondrae",
    "id": 595778
  },
  "clicks" : 10000000
}

db_issue = {
  "html_url": "https://github.com/codeforamerica/gotissues/issues/8",
  "id": 87136867,
  "title": "Pull in data from GitHub about the clicked issues",
  "labels": [
    { "url": "https://api.github.com/repos/codeforamerica/gotissues/labels/enhancement",
      "name": "enhancement",
      "color": "84b6eb"
    }
  ],
  "state": "closed",
  "comments": 1,
  "created_at": "2015-06-10T23:03:05Z",
  "closed_at": "2015-06-23T00:43:26Z",
  "body": "TEST BODY",
  "closed_by": {
    "login": "ondrae",
    "id": 595778
  },
  "clicks" : 10000000,
  "views" : 777,
  "view_sources" : ["www.codeforamerica.org"]
}