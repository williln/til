# Setting output for a step in a job, so a different job can use it 

- In the specific job element (so `create-issue-comment` in the example below), add the field `outputs` 
  - The label for your variable is what you will use to refer to it in other jobs. In the example below, the label is `issue_json`
  - Use the `${{ }}` syntax to access the result of one of the steps in this job. Inside the curly braces, use dot syntax to identify the path to the step's output
   - In the example below, `${{ steps.set-json.outputs.issue_json }}` is looking for one of the `steps` in the current job with an `id` of `set-json` and expecting it to have set an `outputs` called `issue_json`
- In the step with the result you need to save, have it `echo` the variable name you chose in your `outputs` (in this case, `issue_json`) to `$GITHUB_OUTPUT`, a constant that GH uses to catch output. 
  - See [Defining outputs for jobs](https://docs.github.com/en/actions/using-jobs/defining-outputs-for-jobs)
- You have to add the `id` element to your `steps` to refer to them properly 
 
```yaml
name: Process new issues

on:
  issues:
    types: [labeled, opened]

jobs:
  create-issue-comment:
    runs-on: ubuntu-latest

    # The output variables that get created
    outputs:
      issue_json: ${{ steps.set-json.outputs.issue_json }}
    steps:
      # Parse the JSON from the issue body
      - name: Parse issue
        id: parse
        uses: peter-murray/issue-forms-body-parser@v2.0.0
        with:
          issue_id: ${{ github.event.issue.number }}
          separator: '###'
          label_marker_start: '>>'
          label_marker_end: '<<'

      # Save the parsed JSON as output
      - name: Set JSON
        id: set-json
        # Use the `outputs.payload` from the `parse` step 
        run: echo "issue_json=${{ steps.parse.outputs.payload }}" >> $GITHUB_OUTPUT
        
   # This is a new job 
   see-output:
    ## Specify that this job needs the `create-issue-comment` job to run first 
    needs: create-issue-comment
    runs-on: ubuntu-latest
    steps:
      # Access the `issue_json` by traversing the `outputs` of the job identified in `needs`
      - name: Prove we got the link
      
        run: echo "${{ needs.create-issue-comment.outputs.issue_json }}"


```
