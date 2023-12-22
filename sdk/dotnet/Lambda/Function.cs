// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda
{
    /// <summary>
    /// Resource Type definition for AWS::Lambda::Function in region
    /// </summary>
    [AwsNativeResourceType("aws-native:lambda:Function")]
    public partial class Function : global::Pulumi.CustomResource
    {
        [Output("architectures")]
        public Output<ImmutableArray<Pulumi.AwsNative.Lambda.FunctionArchitecturesItem>> Architectures { get; private set; } = null!;

        /// <summary>
        /// Unique identifier for function resources
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The code for the function.
        /// </summary>
        [Output("code")]
        public Output<Outputs.FunctionCode> Code { get; private set; } = null!;

        /// <summary>
        /// A unique Arn for CodeSigningConfig resource
        /// </summary>
        [Output("codeSigningConfigArn")]
        public Output<string?> CodeSigningConfigArn { get; private set; } = null!;

        /// <summary>
        /// A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
        /// </summary>
        [Output("deadLetterConfig")]
        public Output<Outputs.FunctionDeadLetterConfig?> DeadLetterConfig { get; private set; } = null!;

        /// <summary>
        /// A description of the function.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Environment variables that are accessible from function code during execution.
        /// </summary>
        [Output("environment")]
        public Output<Outputs.FunctionEnvironment?> Environment { get; private set; } = null!;

        /// <summary>
        /// A function's ephemeral storage settings.
        /// </summary>
        [Output("ephemeralStorage")]
        public Output<Outputs.FunctionEphemeralStorage?> EphemeralStorage { get; private set; } = null!;

        /// <summary>
        /// Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
        /// </summary>
        [Output("fileSystemConfigs")]
        public Output<ImmutableArray<Outputs.FunctionFileSystemConfig>> FileSystemConfigs { get; private set; } = null!;

        /// <summary>
        /// The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
        /// </summary>
        [Output("functionName")]
        public Output<string?> FunctionName { get; private set; } = null!;

        /// <summary>
        /// The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
        /// </summary>
        [Output("handler")]
        public Output<string?> Handler { get; private set; } = null!;

        /// <summary>
        /// ImageConfig
        /// </summary>
        [Output("imageConfig")]
        public Output<Outputs.FunctionImageConfig?> ImageConfig { get; private set; } = null!;

        /// <summary>
        /// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        /// </summary>
        [Output("kmsKeyArn")]
        public Output<string?> KmsKeyArn { get; private set; } = null!;

        /// <summary>
        /// A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
        /// </summary>
        [Output("layers")]
        public Output<ImmutableArray<string>> Layers { get; private set; } = null!;

        /// <summary>
        /// The logging configuration of your function
        /// </summary>
        [Output("loggingConfig")]
        public Output<Outputs.FunctionLoggingConfig?> LoggingConfig { get; private set; } = null!;

        /// <summary>
        /// The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
        /// </summary>
        [Output("memorySize")]
        public Output<int?> MemorySize { get; private set; } = null!;

        /// <summary>
        /// PackageType.
        /// </summary>
        [Output("packageType")]
        public Output<Pulumi.AwsNative.Lambda.FunctionPackageType?> PackageType { get; private set; } = null!;

        /// <summary>
        /// The number of simultaneous executions to reserve for the function.
        /// </summary>
        [Output("reservedConcurrentExecutions")]
        public Output<int?> ReservedConcurrentExecutions { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the function's execution role.
        /// </summary>
        [Output("role")]
        public Output<string> Role { get; private set; } = null!;

        /// <summary>
        /// The identifier of the function's runtime.
        /// </summary>
        [Output("runtime")]
        public Output<string?> Runtime { get; private set; } = null!;

        /// <summary>
        /// RuntimeManagementConfig
        /// </summary>
        [Output("runtimeManagementConfig")]
        public Output<Outputs.FunctionRuntimeManagementConfig?> RuntimeManagementConfig { get; private set; } = null!;

        /// <summary>
        /// The SnapStart setting of your function
        /// </summary>
        [Output("snapStart")]
        public Output<Outputs.FunctionSnapStart?> SnapStart { get; private set; } = null!;

        /// <summary>
        /// The SnapStart response of your function
        /// </summary>
        [Output("snapStartResponse")]
        public Output<Outputs.FunctionSnapStartResponse> SnapStartResponse { get; private set; } = null!;

        /// <summary>
        /// A list of tags to apply to the function.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.FunctionTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
        /// </summary>
        [Output("timeout")]
        public Output<int?> Timeout { get; private set; } = null!;

        /// <summary>
        /// Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
        /// </summary>
        [Output("tracingConfig")]
        public Output<Outputs.FunctionTracingConfig?> TracingConfig { get; private set; } = null!;

        /// <summary>
        /// For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
        /// </summary>
        [Output("vpcConfig")]
        public Output<Outputs.FunctionVpcConfig?> VpcConfig { get; private set; } = null!;


        /// <summary>
        /// Create a Function resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Function(string name, FunctionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lambda:Function", name, args ?? new FunctionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Function(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lambda:Function", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "functionName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Function resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Function Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Function(name, id, options);
        }
    }

    public sealed class FunctionArgs : global::Pulumi.ResourceArgs
    {
        [Input("architectures")]
        private InputList<Pulumi.AwsNative.Lambda.FunctionArchitecturesItem>? _architectures;
        public InputList<Pulumi.AwsNative.Lambda.FunctionArchitecturesItem> Architectures
        {
            get => _architectures ?? (_architectures = new InputList<Pulumi.AwsNative.Lambda.FunctionArchitecturesItem>());
            set => _architectures = value;
        }

        /// <summary>
        /// The code for the function.
        /// </summary>
        [Input("code", required: true)]
        public Input<Inputs.FunctionCodeArgs> Code { get; set; } = null!;

        /// <summary>
        /// A unique Arn for CodeSigningConfig resource
        /// </summary>
        [Input("codeSigningConfigArn")]
        public Input<string>? CodeSigningConfigArn { get; set; }

        /// <summary>
        /// A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
        /// </summary>
        [Input("deadLetterConfig")]
        public Input<Inputs.FunctionDeadLetterConfigArgs>? DeadLetterConfig { get; set; }

        /// <summary>
        /// A description of the function.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Environment variables that are accessible from function code during execution.
        /// </summary>
        [Input("environment")]
        public Input<Inputs.FunctionEnvironmentArgs>? Environment { get; set; }

        /// <summary>
        /// A function's ephemeral storage settings.
        /// </summary>
        [Input("ephemeralStorage")]
        public Input<Inputs.FunctionEphemeralStorageArgs>? EphemeralStorage { get; set; }

        [Input("fileSystemConfigs")]
        private InputList<Inputs.FunctionFileSystemConfigArgs>? _fileSystemConfigs;

        /// <summary>
        /// Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
        /// </summary>
        public InputList<Inputs.FunctionFileSystemConfigArgs> FileSystemConfigs
        {
            get => _fileSystemConfigs ?? (_fileSystemConfigs = new InputList<Inputs.FunctionFileSystemConfigArgs>());
            set => _fileSystemConfigs = value;
        }

        /// <summary>
        /// The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
        /// </summary>
        [Input("functionName")]
        public Input<string>? FunctionName { get; set; }

        /// <summary>
        /// The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
        /// </summary>
        [Input("handler")]
        public Input<string>? Handler { get; set; }

        /// <summary>
        /// ImageConfig
        /// </summary>
        [Input("imageConfig")]
        public Input<Inputs.FunctionImageConfigArgs>? ImageConfig { get; set; }

        /// <summary>
        /// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        /// </summary>
        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        [Input("layers")]
        private InputList<string>? _layers;

        /// <summary>
        /// A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
        /// </summary>
        public InputList<string> Layers
        {
            get => _layers ?? (_layers = new InputList<string>());
            set => _layers = value;
        }

        /// <summary>
        /// The logging configuration of your function
        /// </summary>
        [Input("loggingConfig")]
        public Input<Inputs.FunctionLoggingConfigArgs>? LoggingConfig { get; set; }

        /// <summary>
        /// The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
        /// </summary>
        [Input("memorySize")]
        public Input<int>? MemorySize { get; set; }

        /// <summary>
        /// PackageType.
        /// </summary>
        [Input("packageType")]
        public Input<Pulumi.AwsNative.Lambda.FunctionPackageType>? PackageType { get; set; }

        /// <summary>
        /// The number of simultaneous executions to reserve for the function.
        /// </summary>
        [Input("reservedConcurrentExecutions")]
        public Input<int>? ReservedConcurrentExecutions { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the function's execution role.
        /// </summary>
        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        /// <summary>
        /// The identifier of the function's runtime.
        /// </summary>
        [Input("runtime")]
        public Input<string>? Runtime { get; set; }

        /// <summary>
        /// RuntimeManagementConfig
        /// </summary>
        [Input("runtimeManagementConfig")]
        public Input<Inputs.FunctionRuntimeManagementConfigArgs>? RuntimeManagementConfig { get; set; }

        /// <summary>
        /// The SnapStart setting of your function
        /// </summary>
        [Input("snapStart")]
        public Input<Inputs.FunctionSnapStartArgs>? SnapStart { get; set; }

        [Input("tags")]
        private InputList<Inputs.FunctionTagArgs>? _tags;

        /// <summary>
        /// A list of tags to apply to the function.
        /// </summary>
        public InputList<Inputs.FunctionTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FunctionTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        /// <summary>
        /// Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
        /// </summary>
        [Input("tracingConfig")]
        public Input<Inputs.FunctionTracingConfigArgs>? TracingConfig { get; set; }

        /// <summary>
        /// For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
        /// </summary>
        [Input("vpcConfig")]
        public Input<Inputs.FunctionVpcConfigArgs>? VpcConfig { get; set; }

        public FunctionArgs()
        {
        }
        public static new FunctionArgs Empty => new FunctionArgs();
    }
}
