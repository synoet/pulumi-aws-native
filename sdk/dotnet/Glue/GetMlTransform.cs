// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    public static class GetMlTransform
    {
        /// <summary>
        /// Resource Type definition for AWS::Glue::MLTransform
        /// </summary>
        public static Task<GetMlTransformResult> InvokeAsync(GetMlTransformArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMlTransformResult>("aws-native:glue:getMlTransform", args ?? new GetMlTransformArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Glue::MLTransform
        /// </summary>
        public static Output<GetMlTransformResult> Invoke(GetMlTransformInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMlTransformResult>("aws-native:glue:getMlTransform", args ?? new GetMlTransformInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMlTransformArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetMlTransformArgs()
        {
        }
        public static new GetMlTransformArgs Empty => new GetMlTransformArgs();
    }

    public sealed class GetMlTransformInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetMlTransformInvokeArgs()
        {
        }
        public static new GetMlTransformInvokeArgs Empty => new GetMlTransformInvokeArgs();
    }


    [OutputType]
    public sealed class GetMlTransformResult
    {
        public readonly string? Description;
        public readonly string? GlueVersion;
        public readonly string? Id;
        public readonly double? MaxCapacity;
        public readonly int? MaxRetries;
        public readonly string? Name;
        public readonly int? NumberOfWorkers;
        public readonly string? Role;
        public readonly object? Tags;
        public readonly int? Timeout;
        public readonly Outputs.MlTransformTransformEncryption? TransformEncryption;
        public readonly Outputs.MlTransformTransformParameters? TransformParameters;
        public readonly string? WorkerType;

        [OutputConstructor]
        private GetMlTransformResult(
            string? description,

            string? glueVersion,

            string? id,

            double? maxCapacity,

            int? maxRetries,

            string? name,

            int? numberOfWorkers,

            string? role,

            object? tags,

            int? timeout,

            Outputs.MlTransformTransformEncryption? transformEncryption,

            Outputs.MlTransformTransformParameters? transformParameters,

            string? workerType)
        {
            Description = description;
            GlueVersion = glueVersion;
            Id = id;
            MaxCapacity = maxCapacity;
            MaxRetries = maxRetries;
            Name = name;
            NumberOfWorkers = numberOfWorkers;
            Role = role;
            Tags = tags;
            Timeout = timeout;
            TransformEncryption = transformEncryption;
            TransformParameters = transformParameters;
            WorkerType = workerType;
        }
    }
}
