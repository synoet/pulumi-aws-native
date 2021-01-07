// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EventSchemas.Outputs
{

    [OutputType]
    public sealed class SchemaProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content
        /// </summary>
        public readonly string Content;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname
        /// </summary>
        public readonly string RegistryName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname
        /// </summary>
        public readonly string? SchemaName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags
        /// </summary>
        public readonly ImmutableArray<Outputs.SchemaTagsEntry> Tags;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private SchemaProperties(
            string Content,

            string? Description,

            string RegistryName,

            string? SchemaName,

            ImmutableArray<Outputs.SchemaTagsEntry> Tags,

            string Type)
        {
            this.Content = Content;
            this.Description = Description;
            this.RegistryName = RegistryName;
            this.SchemaName = SchemaName;
            this.Tags = Tags;
            this.Type = Type;
        }
    }
}