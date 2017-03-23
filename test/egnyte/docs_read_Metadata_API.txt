Node:
(type) c
(layer)0
	Element:body
			Node:
			(type) h1
			(layer)1
				Element:h1
					Metadata API
			Node:
			(type) c
			(layer)1
				Element:p
					The Metadata API allows you to define custom metadata fields and then use those fields to set values on files, file versions, and folders. Metadata fields (keys) are grouped together in namespaces.
			Node:
			(type) c
			(layer)1
				Element:p
					Namespaces can be either private or public. Private namespaces are only visible to the application that created them (i.e. only when accessing with the same Public API key). Public namespaces are visible to any application and are also visible within the Web UI.
			Node:
			(type) c
			(layer)1
				Element:p
				Element:strong
					Note: This API is in beta and is subject to change.
			Node:
			(type) c
			(layer)1
												Node:
												(type) c
												(layer)4
													Element:h4
														Common HTTP Headers
												Node:
												(type) c
												(layer)4
													Element:table
													Element:tbody
													Element:tr
													Element:th
														Header
													Element:th
														Description
													Element:th
														Value
													Element:tr
													Element:td
													Element:span
														Content-Type
													Element:td
														Specifies the format of the request body
													Element:td
														application/json
													Element:tr
													Element:td
													Element:span
														Authorization
													Element:td
														Requires the OAuth token you obtained through the OAuth flow
													Element:td
														Bearer {OAuth token}
												Node:
												(type) c
												(layer)4
													Element:table
													Element:tbody
													Element:tr
													Element:th
														Error
													Element:th
														Description
													Element:tr
													Element:td
													Element:span
														200
													Element:td
														Successful operation
													Element:tr
													Element:td
													Element:span
														403
													Element:td
														User is not authorized
													Element:tr
													Element:td
													Element:span
														404
													Element:td
														Item not found
												Node:
												(type) c
												(layer)4
													Element:p
													Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Get All Namespaces
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to list all custom metadata namespaces in the domain.
									Node:
									(type) c
									(layer)3
										Element:span
											GET
											/pubapi/v1/properties/namespace
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Create Namespace
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to create a namespace of custom metadata fields for a domain.
									Node:
									(type) c
									(layer)3
										Element:span
											POST
											/pubapi/v1/properties/namespace
									Node:
									(type) c
									(layer)3
										Element:h4
											Request Parameters
									Node:
									(type) c
									(layer)3
										Element:table
										Element:tbody
										Element:tr
										Element:th
											Parameter
										Element:th
											Description
										Element:th
											Required
										Element:th
											Possible Values
										Element:tr
										Element:td
										Element:span
											name
										Element:td
											What you call the namespace
										Element:td
											Yes
										Element:td
											string
										Element:tr
										Element:td
										Element:span
											displayName
										Element:td
											The name to identify the namespace in the UI
										Element:td
											No
										Element:td
											string
										Element:tr
										Element:td
										Element:span
											scope
										Element:td
											Who can see and modify the namespace
										Element:td
											Yes
										Element:td
											public, private
										Element:tr
										Element:td
										Element:span
											keys
										Element:td
											The custom metadata key(s) you are creating
										Element:td
											Yes
										Element:td
											JSON object (see create metadata key endpoint for fields)
										Element:tr
										Element:td
										Element:span
											type
										Element:td
											Specifies the data type for a key.
										Element:td
											Yes
										Element:td
											integer, string, decimal, date, enum
										Element:tr
										Element:td
										Element:span
											data
										Element:td
											For a key of enum type, specifies the enumerated values.
										Element:td
											Only required for enum
										Element:td
											E.g. ["red", "green", "blue"]
										Element:tr
										Element:td
										Element:span
											helpText
										Element:td
											Instructional text that is displayed when a user is adding/editing a property to give context as to the property's purpose
										Element:td
											No
										Element:td
											string
									Node:
									(type) c
									(layer)3
										Element:h4
											Sample Request Body
									Node:
									(type) c
									(layer)3
										Element:pre
											{ "name": "namespace1", "scope": "public", "displayName": "my first namespace", "keys": { "int-key": { "type": "integer", "displayName": "my key" }, "decimal-key": { "type": "decimal" }, "string-key": { "type": "string" }, "enum-key": { "type": "enum", "data": ["val1", "val2"] }, "date-key": { "type": "string" } } }
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Update Namespace Values
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to update the namespace scope or name of a custom metadata for a domain.
									Node:
									(type) c
									(layer)3
										Element:span
											PATCH
											/pubapi/v1/properties/namespace/{namespace name}
									Node:
									(type) c
									(layer)3
										Element:h4
											Request Parameters
									Node:
									(type) c
									(layer)3
										Element:table
										Element:tbody
										Element:tr
										Element:th
											Parameter
										Element:th
											Description
										Element:th
											Required
										Element:th
											Possible Values
										Element:tr
										Element:td
										Element:span
											displayName
										Element:td
											The name to identify the namespace in the UI
										Element:td
											No
										Element:td
											string
										Element:tr
										Element:td
										Element:span
											scope
										Element:td
											Who can see and modify the namespace
										Element:td
											No
										Element:td
											public, private
									Node:
									(type) c
									(layer)3
										Element:h4
											Sample Request Body
									Node:
									(type) c
									(layer)3
										Element:pre
											{ "scope": "public", "displayName": "a namespace with a new name" }
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Update Namespace Keys
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to update the key definitions of a namespace of custom metadata fields for a domain.
									Node:
									(type) c
									(layer)3
										Element:span
											PATCH
											/pubapi/v1/properties/namespace/{namespace name}/keys/{key name}
									Node:
									(type) c
									(layer)3
										Element:h4
											Request Parameters
									Node:
									(type) c
									(layer)3
										Element:table
										Element:tbody
										Element:tr
										Element:th
											Parameter
										Element:th
											Description
										Element:th
											Required
										Element:th
											Possible Values
										Element:tr
										Element:td
										Element:span
											displayName
										Element:td
											Specifies the name displayed for the key
										Element:td
											No
										Element:td
											string
										Element:tr
										Element:td
										Element:span
											type
										Element:td
											Specifies the data type for a key. Can only allow a change to a broader type:
										Element:ul
										Element:li
											decimal -> string
										Element:li
											integer -> string, decimal
										Element:li
											date -> string, decimal, integer
										Element:li
											enum -> string (in this case the 'data' parameter will be automatically set to null)
										Element:td
											No
										Element:td
											integer, string, decimal, date, enum
										Element:tr
										Element:td
										Element:span
											data
										Element:td
											For a key of enum type, specifies the enumerated values. Only new values are allowed
										Element:td
											Only required for enum
										Element:td
											E.g. ["red", "green", "blue"]
										Element:tr
										Element:td
										Element:span
											helpText
										Element:td
											Instructional text that is displayed when a user is adding/editing a property to give context as to the property's purpose
										Element:td
											No
										Element:td
											string
									Node:
									(type) c
									(layer)3
										Element:h4
											Sample Request Body
									Node:
									(type) c
									(layer)3
										Element:pre
											{ "displayName": "My new display name", "helpText": "Use this key", "data": ["red", "green", "blue", "new color"], "type": "enum" }
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Get Namespace
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to list all custom metadata keys that have been created in a given namespace.
									Node:
									(type) c
									(layer)3
										Element:span
											GET
											/pubapi/v1/properties/namespace/{namespace name}
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Delete Namespace
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to delete a specified namespace. This is only possible if the namespace is not in use.
									Node:
									(type) c
									(layer)3
										Element:span
											DELETE
											/pubapi/v1/properties/namespace/{namespace name}
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Create Metadata Key
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to add a metadata key to an existing namespace.
									Node:
									(type) c
									(layer)3
										Element:span
											POST
											/pubapi/v1/properties/namespace/{namespace name}/keys
									Node:
									(type) c
									(layer)3
										Element:h4
											Request Parameters
									Node:
									(type) c
									(layer)3
										Element:table
										Element:tbody
										Element:tr
										Element:th
											Parameter
										Element:th
											Description
										Element:th
											Required
										Element:th
											Possible Values
										Element:tr
										Element:td
										Element:span
											key
										Element:td
											The name of the key you are creating
										Element:td
											Yes
										Element:td
											string
										Element:tr
										Element:td
										Element:span
											type
										Element:td
											Specifies the data type for a key.
										Element:td
											Yes
										Element:td
											integer, string, decimal, date, enum
										Element:tr
										Element:td
										Element:span
											displayName
										Element:td
											The name to identify the field in the UI.
										Element:td
											No
										Element:td
											string
										Element:tr
										Element:td
										Element:span
											helpText
										Element:td
											A tooltip description for the metadata field.
										Element:td
											No
										Element:td
											string
										Element:tr
										Element:td
										Element:span
											data
										Element:td
											For a key of enum type, specifies the enumerated values.
										Element:td
											Only required for enum
										Element:td
											E.g. ["red", "green", "blue"]
									Node:
									(type) c
									(layer)3
										Element:h4
											Sample Request Body
									Node:
									(type) c
									(layer)3
										Element:pre
											{ "key": "new-enum-key", "type": "enum", "data": ["red", "green", "blue"], "displayName": "My new key for values", "helpText": "Use this key to tag files with these values" }
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Delete Metadata Key
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to delete a metadata key from an existing namespace. This is only possible if the namespace is not in use.
									Node:
									(type) c
									(layer)3
										Element:span
											DELETE
											/pubapi/v1/properties/namespace/{namespace name}/keys/{key name}
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Set Values for a Namespace
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to set a metadata values for a given namespace for a file, file version, or folder. This endpoint allows multiple key/value pairs to be set at once. If the key already has a value, the old value will be overriden by the new value. If the value for a key is set to null, the existing value will be removed. For more information on interacting with files, specific file versions, or folders, please refer to the
										Element:a
											File System API documentation
											.
									Node:
									(type) c
									(layer)3
										Element:p
											To set a metadata value for a file, use the group ID of the file. To set a metadata value for a specific file version, use the entry ID of the file version. To set a metadata value for a folder, use the folder ID.
									Node:
									(type) c
									(layer)3
										Element:ul
										Element:li
										Element:a
											File
										Element:li
										Element:a
											Folder
									Node:
									(type) c
									(layer)3
										Element:span
											PUT
											/pubapi/v1/fs/ids/file/{group_id or entry_id}/properties/{namespace name}
									Node:
									(type) c
									(layer)3
										Element:span
											PUT
											/pubapi/v1/fs/ids/folder/{folder_id}/properties/{namespace name}
									Node:
									(type) c
									(layer)3
										Element:h4
											Sample Request Body
									Node:
									(type) c
									(layer)3
										Element:pre
											{ "string-key": "abc", "int-key": "10", "date-key": "1465413843995" }
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Get Values for a Namespace
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to get the metadata values for a given namespace for a file, file version, or folder. For more information on interacting with files, specific file versions, or folders, please refer to the
										Element:a
											File System API documentation
											.
									Node:
									(type) c
									(layer)3
										Element:ul
										Element:li
										Element:a
											File
										Element:li
										Element:a
											Folder
									Node:
									(type) c
									(layer)3
										Element:span
											GET
											/pubapi/v1/fs/ids/file/{group_id or entry_id}/properties/{namespace name}
									Node:
									(type) c
									(layer)3
										Element:span
											GET
											/pubapi/v1/fs/ids/folder/{folder_id}/properties/{namespace name}
									Node:
									(type) c
									(layer)3
										Element:h4
											Sample Respose Body
									Node:
									(type) c
									(layer)3
										Element:pre
											{ "results": [ { "workspace": { "string-key": "abc", "int-key": 10 } } ] }
									Node:
									(type) c
									(layer)3
										Element:p
										Element:a
												Node:
												(type) c
												(layer)4
									Node:
									(type) c
									(layer)3
										Element:h3
										Element:span
											Search Metadata
									Node:
									(type) c
									(layer)3
										Element:p
											This endpoint is used to find items that have a specific metadata field or to find items that have a field that contains a specific value.
									Node:
									(type) c
									(layer)3
										Element:span
											POST
											/pubapi/v1/search
									Node:
									(type) c
									(layer)3
										Element:h4
											Request Parameters
									Node:
									(type) c
									(layer)3
										Element:table
										Element:tbody
										Element:tr
										Element:th
											Parameter
										Element:th
											Description
										Element:th
											Required
										Element:th
											Possible Values
										Element:tr
										Element:td
										Element:span
											type
										Element:td
											Which item types should be searched
										Element:td
											No
										Element:td
											ALL, FOLDER, FILE
										Element:tr
										Element:td
										Element:span
											has_key
										Element:td
											Allows for finding items that have a specific key. If multiple objects are included in the array, any item matching one or more of the conditions will be returned.
										Element:td
											No
										Element:td
											An array of objects with keys "namespace" and "key", e.g. [{"namespace": "namespace1", key: "string-key"}]
										Element:tr
										Element:td
										Element:span
											key_with_value
										Element:td
											Allows for finding items that contain a specific string within a metadata value for a specified field. Note that this is not an exact match, but rather looks for any string that contains the search term. If multiple objects are included in the array, any item matching one or more of the conditions will be returned.
										Element:td
											No
										Element:td
											An array of objects with keys "namespace", "key", and "value", e.g. [{"namespace": "namespace1", key: "string-key", "value": "abc"}]
									Node:
									(type) c
									(layer)3
										Element:h4
											Sample Request Body
									Node:
									(type) c
									(layer)3
										Element:pre
											{ "type": "ALL", "key_with_value": [ { "namespace": "namespace1", "key": "string-key", "value": "abc" } ] }
									Node:
									(type) c
									(layer)3
										Element:p
										Element:span
											version 31
										Element:span
											as of
										Element:abbr
											2 months ago
										Element:span
											by
										Element:span
										Element:a
											Greg Neustaetter
									Node:
									(type) c
									(layer)3
										Element:ul
										Element:li
										Element:span
											Previous:
										Element:a
											Comments API
										Element:li
										Element:span
											Up:
										Element:a
											Overview
										Element:li
										Element:span
											Next:
										Element:a
											Embedded UI API
									Node:
									(type) c
									(layer)3
						Node:
						(type) c
						(layer)2
							Element:h2
								Docs Navigation
						Node:
						(type) c
						(layer)2
							Element:ul
							Element:li
							Element:a
								Overview
							Element:li
							Element:a
								Getting Started
							Element:li
							Element:a
								Authentication
							Element:li
							Element:a
								File System API
							Element:li
							Element:a
								Permissions API
							Element:li
							Element:a
								Events API
							Element:li
							Element:a
								Search API
							Element:li
							Element:a
								Links API
							Element:li
							Element:a
								User Management API
							Element:li
							Element:a
								Group Management API
							Element:li
							Element:a
								Audit Reporting API
							Element:li
							Element:a
								UI Integration Framework
							Element:li
							Element:a
								Trash API
							Element:li
							Element:a
								Comments API
							Element:li
							Element:a
								Metadata API
							Element:li
							Element:a
								Embedded UI API
							Element:li
							Element:a
								Bookmarks API
							Element:li
							Element:a
								Folder Options API
							Element:li
							Element:a
								Best Practices
						Node:
						(type) c
						(layer)2
							Element:ul
							Element:li
							Element:a
								Get API Key
							Element:li
							Element:a
								API Docs
							Element:li
							Element:a
								Getting Started
							Element:li
							Element:a
								Explore APIs
							Element:li
							Element:a
								Explore SDKs
						Node:
						(type) c
						(layer)2
							Element:noscript
							Element:img
