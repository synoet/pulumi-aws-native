// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EventSchemas
{
    public static class GetSchema
    {
        /// <summary>
        /// Resource Type definition for AWS::EventSchemas::Schema
        /// </summary>
        public static Task<GetSchemaResult> InvokeAsync(GetSchemaArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSchemaResult>("aws-native:eventschemas:getSchema", args ?? new GetSchemaArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EventSchemas::Schema
        /// </summary>
        public static Output<GetSchemaResult> Invoke(GetSchemaInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSchemaResult>("aws-native:eventschemas:getSchema", args ?? new GetSchemaInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSchemaArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the schema.
        /// </summary>
        [Input("schemaArn", required: true)]
        public string SchemaArn { get; set; } = null!;

        public GetSchemaArgs()
        {
        }
        public static new GetSchemaArgs Empty => new GetSchemaArgs();
    }

    public sealed class GetSchemaInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the schema.
        /// </summary>
        [Input("schemaArn", required: true)]
        public Input<string> SchemaArn { get; set; } = null!;

        public GetSchemaInvokeArgs()
        {
        }
        public static new GetSchemaInvokeArgs Empty => new GetSchemaInvokeArgs();
    }


    [OutputType]
    public sealed class GetSchemaResult
    {
        /// <summary>
        /// The source of the schema definition.
        /// </summary>
        public readonly string? Content;
        /// <summary>
        /// A description of the schema.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The last modified time of the schema.
        /// </summary>
        public readonly string? LastModified;
        /// <summary>
        /// The ARN of the schema.
        /// </summary>
        public readonly string? SchemaArn;
        /// <summary>
        /// The version number of the schema.
        /// </summary>
        public readonly string? SchemaVersion;
        /// <summary>
        /// Tags associated with the resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.SchemaTagsEntry> Tags;
        /// <summary>
        /// The type of schema. Valid types include OpenApi3 and JSONSchemaDraft4.
        /// </summary>
        public readonly string? Type;
        /// <summary>
        /// The date the schema version was created.
        /// </summary>
        public readonly string? VersionCreatedDate;

        [OutputConstructor]
        private GetSchemaResult(
            string? content,

            string? description,

            string? lastModified,

            string? schemaArn,

            string? schemaVersion,

            ImmutableArray<Outputs.SchemaTagsEntry> tags,

            string? type,

            string? versionCreatedDate)
        {
            Content = content;
            Description = description;
            LastModified = lastModified;
            SchemaArn = schemaArn;
            SchemaVersion = schemaVersion;
            Tags = tags;
            Type = type;
            VersionCreatedDate = versionCreatedDate;
        }
    }
}
