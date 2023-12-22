// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Dms
{
    public static class GetMigrationProject
    {
        /// <summary>
        /// Resource schema for AWS::DMS::MigrationProject
        /// </summary>
        public static Task<GetMigrationProjectResult> InvokeAsync(GetMigrationProjectArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMigrationProjectResult>("aws-native:dms:getMigrationProject", args ?? new GetMigrationProjectArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::DMS::MigrationProject
        /// </summary>
        public static Output<GetMigrationProjectResult> Invoke(GetMigrationProjectInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMigrationProjectResult>("aws-native:dms:getMigrationProject", args ?? new GetMigrationProjectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMigrationProjectArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The property describes an ARN of the migration project.
        /// </summary>
        [Input("migrationProjectArn", required: true)]
        public string MigrationProjectArn { get; set; } = null!;

        public GetMigrationProjectArgs()
        {
        }
        public static new GetMigrationProjectArgs Empty => new GetMigrationProjectArgs();
    }

    public sealed class GetMigrationProjectInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The property describes an ARN of the migration project.
        /// </summary>
        [Input("migrationProjectArn", required: true)]
        public Input<string> MigrationProjectArn { get; set; } = null!;

        public GetMigrationProjectInvokeArgs()
        {
        }
        public static new GetMigrationProjectInvokeArgs Empty => new GetMigrationProjectInvokeArgs();
    }


    [OutputType]
    public sealed class GetMigrationProjectResult
    {
        /// <summary>
        /// The optional description of the migration project.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The property describes an instance profile arn for the migration project. For read
        /// </summary>
        public readonly string? InstanceProfileArn;
        /// <summary>
        /// The property describes an instance profile name for the migration project. For read
        /// </summary>
        public readonly string? InstanceProfileName;
        /// <summary>
        /// The property describes an ARN of the migration project.
        /// </summary>
        public readonly string? MigrationProjectArn;
        /// <summary>
        /// The property describes a creating time of the migration project.
        /// </summary>
        public readonly string? MigrationProjectCreationTime;
        /// <summary>
        /// The property describes a name to identify the migration project.
        /// </summary>
        public readonly string? MigrationProjectName;
        /// <summary>
        /// The property describes schema conversion application attributes for the migration project.
        /// </summary>
        public readonly Outputs.SchemaConversionApplicationAttributesProperties? SchemaConversionApplicationAttributes;
        /// <summary>
        /// The property describes source data provider descriptors for the migration project.
        /// </summary>
        public readonly ImmutableArray<Outputs.MigrationProjectDataProviderDescriptor> SourceDataProviderDescriptors;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.MigrationProjectTag> Tags;
        /// <summary>
        /// The property describes target data provider descriptors for the migration project.
        /// </summary>
        public readonly ImmutableArray<Outputs.MigrationProjectDataProviderDescriptor> TargetDataProviderDescriptors;
        /// <summary>
        /// The property describes transformation rules for the migration project.
        /// </summary>
        public readonly string? TransformationRules;

        [OutputConstructor]
        private GetMigrationProjectResult(
            string? description,

            string? instanceProfileArn,

            string? instanceProfileName,

            string? migrationProjectArn,

            string? migrationProjectCreationTime,

            string? migrationProjectName,

            Outputs.SchemaConversionApplicationAttributesProperties? schemaConversionApplicationAttributes,

            ImmutableArray<Outputs.MigrationProjectDataProviderDescriptor> sourceDataProviderDescriptors,

            ImmutableArray<Outputs.MigrationProjectTag> tags,

            ImmutableArray<Outputs.MigrationProjectDataProviderDescriptor> targetDataProviderDescriptors,

            string? transformationRules)
        {
            Description = description;
            InstanceProfileArn = instanceProfileArn;
            InstanceProfileName = instanceProfileName;
            MigrationProjectArn = migrationProjectArn;
            MigrationProjectCreationTime = migrationProjectCreationTime;
            MigrationProjectName = migrationProjectName;
            SchemaConversionApplicationAttributes = schemaConversionApplicationAttributes;
            SourceDataProviderDescriptors = sourceDataProviderDescriptors;
            Tags = tags;
            TargetDataProviderDescriptors = targetDataProviderDescriptors;
            TransformationRules = transformationRules;
        }
    }
}
