# API Specification (Version 1; v1)

## Notes

All URLs prefaced by '/v1/' for this version of the API.

## Endpoints

Endpoint definitions are structured roughly like so:
* Intended functionality
* Example URL
* URL parameters
* Request Type
* Request Parameters
* Response Parameters

All requests and responses are expected to be performed in JSON for this API version.

**Standard Endpoint Response Fields**

All endpoints will return, on receipt of a request (invalid or otherwise), the following fields at minimum:
* `success`: Boolean value
* `code`: Integer error code

Error codes are defined in another document

### auth

### get

#### mood

Retrieves a set of mood values taken within a given interval.

Example: `/v1/get/mood`
URL Parameters: None
Request Type: POST

Request Parameters:
* `start`: Encoded date/time specifying start of interval
* `end`: Encoded date/time specifying end of interval

Response Parameters:
* `moods`: A list of mood values, ordered by time, with the following format:
	* `value`: Integer mood value
	* `time` : Encoded time of recording

### put