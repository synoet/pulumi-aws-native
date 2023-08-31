// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Lambda::Function in region
 */
export class Function extends pulumi.CustomResource {
    /**
     * Get an existing Function resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Function {
        return new Function(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lambda:Function';

    /**
     * Returns true if the given object is an instance of Function.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Function {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Function.__pulumiType;
    }

    public readonly architectures!: pulumi.Output<enums.lambda.FunctionArchitecturesItem[] | undefined>;
    /**
     * Unique identifier for function resources
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The code for the function.
     */
    public readonly code!: pulumi.Output<outputs.lambda.FunctionCode>;
    /**
     * A unique Arn for CodeSigningConfig resource
     */
    public readonly codeSigningConfigArn!: pulumi.Output<string | undefined>;
    /**
     * A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
     */
    public readonly deadLetterConfig!: pulumi.Output<outputs.lambda.FunctionDeadLetterConfig | undefined>;
    /**
     * A description of the function.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Environment variables that are accessible from function code during execution.
     */
    public readonly environment!: pulumi.Output<outputs.lambda.FunctionEnvironment | undefined>;
    /**
     * A function's ephemeral storage settings.
     */
    public readonly ephemeralStorage!: pulumi.Output<outputs.lambda.FunctionEphemeralStorage | undefined>;
    /**
     * Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
     */
    public readonly fileSystemConfigs!: pulumi.Output<outputs.lambda.FunctionFileSystemConfig[] | undefined>;
    /**
     * The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
     */
    public readonly functionName!: pulumi.Output<string | undefined>;
    /**
     * The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
     */
    public readonly handler!: pulumi.Output<string | undefined>;
    /**
     * ImageConfig
     */
    public readonly imageConfig!: pulumi.Output<outputs.lambda.FunctionImageConfig | undefined>;
    /**
     * The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
     */
    public readonly kmsKeyArn!: pulumi.Output<string | undefined>;
    /**
     * A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
     */
    public readonly layers!: pulumi.Output<string[] | undefined>;
    /**
     * The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
     */
    public readonly memorySize!: pulumi.Output<number | undefined>;
    /**
     * PackageType.
     */
    public readonly packageType!: pulumi.Output<enums.lambda.FunctionPackageType | undefined>;
    /**
     * The number of simultaneous executions to reserve for the function.
     */
    public readonly reservedConcurrentExecutions!: pulumi.Output<number | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the function's execution role.
     */
    public readonly role!: pulumi.Output<string>;
    /**
     * The identifier of the function's runtime.
     */
    public readonly runtime!: pulumi.Output<string | undefined>;
    /**
     * RuntimeManagementConfig
     */
    public readonly runtimeManagementConfig!: pulumi.Output<outputs.lambda.FunctionRuntimeManagementConfig | undefined>;
    /**
     * The SnapStart setting of your function
     */
    public readonly snapStart!: pulumi.Output<outputs.lambda.FunctionSnapStart | undefined>;
    /**
     * The SnapStart response of your function
     */
    public /*out*/ readonly snapStartResponse!: pulumi.Output<outputs.lambda.FunctionSnapStartResponse>;
    /**
     * A list of tags to apply to the function.
     */
    public readonly tags!: pulumi.Output<outputs.lambda.FunctionTag[] | undefined>;
    /**
     * The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
     */
    public readonly timeout!: pulumi.Output<number | undefined>;
    /**
     * Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
     */
    public readonly tracingConfig!: pulumi.Output<outputs.lambda.FunctionTracingConfig | undefined>;
    /**
     * For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
     */
    public readonly vpcConfig!: pulumi.Output<outputs.lambda.FunctionVpcConfig | undefined>;

    /**
     * Create a Function resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FunctionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.code === undefined) && !opts.urn) {
                throw new Error("Missing required property 'code'");
            }
            if ((!args || args.role === undefined) && !opts.urn) {
                throw new Error("Missing required property 'role'");
            }
            resourceInputs["architectures"] = args ? args.architectures : undefined;
            resourceInputs["code"] = args ? args.code : undefined;
            resourceInputs["codeSigningConfigArn"] = args ? args.codeSigningConfigArn : undefined;
            resourceInputs["deadLetterConfig"] = args ? args.deadLetterConfig : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["environment"] = args ? args.environment : undefined;
            resourceInputs["ephemeralStorage"] = args ? args.ephemeralStorage : undefined;
            resourceInputs["fileSystemConfigs"] = args ? args.fileSystemConfigs : undefined;
            resourceInputs["functionName"] = args ? args.functionName : undefined;
            resourceInputs["handler"] = args ? args.handler : undefined;
            resourceInputs["imageConfig"] = args ? args.imageConfig : undefined;
            resourceInputs["kmsKeyArn"] = args ? args.kmsKeyArn : undefined;
            resourceInputs["layers"] = args ? args.layers : undefined;
            resourceInputs["memorySize"] = args ? args.memorySize : undefined;
            resourceInputs["packageType"] = args ? args.packageType : undefined;
            resourceInputs["reservedConcurrentExecutions"] = args ? args.reservedConcurrentExecutions : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
            resourceInputs["runtime"] = args ? args.runtime : undefined;
            resourceInputs["runtimeManagementConfig"] = args ? args.runtimeManagementConfig : undefined;
            resourceInputs["snapStart"] = args ? args.snapStart : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["timeout"] = args ? args.timeout : undefined;
            resourceInputs["tracingConfig"] = args ? args.tracingConfig : undefined;
            resourceInputs["vpcConfig"] = args ? args.vpcConfig : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["snapStartResponse"] = undefined /*out*/;
        } else {
            resourceInputs["architectures"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["code"] = undefined /*out*/;
            resourceInputs["codeSigningConfigArn"] = undefined /*out*/;
            resourceInputs["deadLetterConfig"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["environment"] = undefined /*out*/;
            resourceInputs["ephemeralStorage"] = undefined /*out*/;
            resourceInputs["fileSystemConfigs"] = undefined /*out*/;
            resourceInputs["functionName"] = undefined /*out*/;
            resourceInputs["handler"] = undefined /*out*/;
            resourceInputs["imageConfig"] = undefined /*out*/;
            resourceInputs["kmsKeyArn"] = undefined /*out*/;
            resourceInputs["layers"] = undefined /*out*/;
            resourceInputs["memorySize"] = undefined /*out*/;
            resourceInputs["packageType"] = undefined /*out*/;
            resourceInputs["reservedConcurrentExecutions"] = undefined /*out*/;
            resourceInputs["role"] = undefined /*out*/;
            resourceInputs["runtime"] = undefined /*out*/;
            resourceInputs["runtimeManagementConfig"] = undefined /*out*/;
            resourceInputs["snapStart"] = undefined /*out*/;
            resourceInputs["snapStartResponse"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["timeout"] = undefined /*out*/;
            resourceInputs["tracingConfig"] = undefined /*out*/;
            resourceInputs["vpcConfig"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["functionName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Function.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Function resource.
 */
export interface FunctionArgs {
    architectures?: pulumi.Input<pulumi.Input<enums.lambda.FunctionArchitecturesItem>[]>;
    /**
     * The code for the function.
     */
    code: pulumi.Input<inputs.lambda.FunctionCodeArgs>;
    /**
     * A unique Arn for CodeSigningConfig resource
     */
    codeSigningConfigArn?: pulumi.Input<string>;
    /**
     * A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
     */
    deadLetterConfig?: pulumi.Input<inputs.lambda.FunctionDeadLetterConfigArgs>;
    /**
     * A description of the function.
     */
    description?: pulumi.Input<string>;
    /**
     * Environment variables that are accessible from function code during execution.
     */
    environment?: pulumi.Input<inputs.lambda.FunctionEnvironmentArgs>;
    /**
     * A function's ephemeral storage settings.
     */
    ephemeralStorage?: pulumi.Input<inputs.lambda.FunctionEphemeralStorageArgs>;
    /**
     * Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
     */
    fileSystemConfigs?: pulumi.Input<pulumi.Input<inputs.lambda.FunctionFileSystemConfigArgs>[]>;
    /**
     * The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
     */
    functionName?: pulumi.Input<string>;
    /**
     * The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
     */
    handler?: pulumi.Input<string>;
    /**
     * ImageConfig
     */
    imageConfig?: pulumi.Input<inputs.lambda.FunctionImageConfigArgs>;
    /**
     * The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
     */
    kmsKeyArn?: pulumi.Input<string>;
    /**
     * A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
     */
    layers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
     */
    memorySize?: pulumi.Input<number>;
    /**
     * PackageType.
     */
    packageType?: pulumi.Input<enums.lambda.FunctionPackageType>;
    /**
     * The number of simultaneous executions to reserve for the function.
     */
    reservedConcurrentExecutions?: pulumi.Input<number>;
    /**
     * The Amazon Resource Name (ARN) of the function's execution role.
     */
    role: pulumi.Input<string>;
    /**
     * The identifier of the function's runtime.
     */
    runtime?: pulumi.Input<string>;
    /**
     * RuntimeManagementConfig
     */
    runtimeManagementConfig?: pulumi.Input<inputs.lambda.FunctionRuntimeManagementConfigArgs>;
    /**
     * The SnapStart setting of your function
     */
    snapStart?: pulumi.Input<inputs.lambda.FunctionSnapStartArgs>;
    /**
     * A list of tags to apply to the function.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.lambda.FunctionTagArgs>[]>;
    /**
     * The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
     */
    timeout?: pulumi.Input<number>;
    /**
     * Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
     */
    tracingConfig?: pulumi.Input<inputs.lambda.FunctionTracingConfigArgs>;
    /**
     * For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
     */
    vpcConfig?: pulumi.Input<inputs.lambda.FunctionVpcConfigArgs>;
}
