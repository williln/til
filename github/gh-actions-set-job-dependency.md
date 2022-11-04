# Making one job in a workflow depend on another job 

See [Workflow Syntax: `jobs.<job_id>.needs`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds). 

> Use `jobs.<job_id>.needs` to identify any jobs that must complete successfully before this job will run. It can be a string or array of strings. If a job fails, all jobs that need it are skipped unless the jobs use a conditional expression that causes the job to continue. If a run contains a series of jobs that need each other, a failure applies to all jobs in the dependency chain from the point of failure onwards.

In the example below, the `see-output` requires that the `create-issue-comment` job complete first, before it will execute. 

```yaml
name: Process new issues

on:
  issues:
    types: opened

jobs:
  create-issue-comment:
    runs-on: ubuntu-latest
    outputs:
      issue_json: ${{ steps.set-json.outputs.issue_json }}
    steps:
      - name: Parse issue
        id: parse
        uses: peter-murray/issue-forms-body-parser@v2.0.0
        with:
          issue_id: ${{ github.event.issue.number }}
          separator: '###'
          label_marker_start: '>>'
          label_marker_end: '<<'
      - name: Set JSON
        id: set-json
        run: echo "issue_json=${{ steps.parse.outputs.payload }}" >> $GITHUB_OUTPUT

  see-output:
    # Specify that `create-issue-comment` should run first 
    needs: create-issue-comment
    runs-on: ubuntu-latest
    steps:
      - name: Prove we got the output 
        run: echo "${{ needs.create-issue-comment.outputs.issue_json }}"

```
