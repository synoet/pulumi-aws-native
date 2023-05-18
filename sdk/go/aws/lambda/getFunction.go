// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Lambda::Function
func LookupFunction(ctx *pulumi.Context, args *LookupFunctionArgs, opts ...pulumi.InvokeOption) (*LookupFunctionResult, error) {
	var rv LookupFunctionResult
	err := ctx.Invoke("aws-native:lambda:getFunction", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupFunctionArgs struct {
	// The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
	FunctionName string `pulumi:"functionName"`
}

type LookupFunctionResult struct {
	Architectures []FunctionArchitecturesItem `pulumi:"architectures"`
	// Unique identifier for function resources
	Arn *string `pulumi:"arn"`
	// A unique Arn for CodeSigningConfig resource
	CodeSigningConfigArn *string `pulumi:"codeSigningConfigArn"`
	// A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
	DeadLetterConfig *FunctionDeadLetterConfig `pulumi:"deadLetterConfig"`
	// A description of the function.
	Description *string `pulumi:"description"`
	// Environment variables that are accessible from function code during execution.
	Environment *FunctionEnvironment `pulumi:"environment"`
	// A function's ephemeral storage settings.
	EphemeralStorage *FunctionEphemeralStorage `pulumi:"ephemeralStorage"`
	// Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
	FileSystemConfigs []FunctionFileSystemConfig `pulumi:"fileSystemConfigs"`
	// The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
	Handler *string `pulumi:"handler"`
	// ImageConfig
	ImageConfig *FunctionImageConfig `pulumi:"imageConfig"`
	// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
	KmsKeyArn *string `pulumi:"kmsKeyArn"`
	// A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
	Layers []string `pulumi:"layers"`
	// The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
	MemorySize *int `pulumi:"memorySize"`
	// PackageType.
	PackageType *FunctionPackageType `pulumi:"packageType"`
	// The number of simultaneous executions to reserve for the function.
	ReservedConcurrentExecutions *int `pulumi:"reservedConcurrentExecutions"`
	// The Amazon Resource Name (ARN) of the function's execution role.
	Role *string `pulumi:"role"`
	// The identifier of the function's runtime.
	Runtime *string `pulumi:"runtime"`
	// RuntimeManagementConfig
	RuntimeManagementConfig *FunctionRuntimeManagementConfig `pulumi:"runtimeManagementConfig"`
	// The SnapStart setting of your function
	SnapStart *FunctionSnapStart `pulumi:"snapStart"`
	// The SnapStart response of your function
	SnapStartResponse *FunctionSnapStartResponse `pulumi:"snapStartResponse"`
	// A list of tags to apply to the function.
	Tags []FunctionTag `pulumi:"tags"`
	// The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
	Timeout *int `pulumi:"timeout"`
	// Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
	TracingConfig *FunctionTracingConfig `pulumi:"tracingConfig"`
	// For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
	VpcConfig *FunctionVpcConfig `pulumi:"vpcConfig"`
}

func LookupFunctionOutput(ctx *pulumi.Context, args LookupFunctionOutputArgs, opts ...pulumi.InvokeOption) LookupFunctionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupFunctionResult, error) {
			args := v.(LookupFunctionArgs)
			r, err := LookupFunction(ctx, &args, opts...)
			var s LookupFunctionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupFunctionResultOutput)
}

type LookupFunctionOutputArgs struct {
	// The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
	FunctionName pulumi.StringInput `pulumi:"functionName"`
}

func (LookupFunctionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFunctionArgs)(nil)).Elem()
}

type LookupFunctionResultOutput struct{ *pulumi.OutputState }

func (LookupFunctionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFunctionResult)(nil)).Elem()
}

func (o LookupFunctionResultOutput) ToLookupFunctionResultOutput() LookupFunctionResultOutput {
	return o
}

func (o LookupFunctionResultOutput) ToLookupFunctionResultOutputWithContext(ctx context.Context) LookupFunctionResultOutput {
	return o
}

func (o LookupFunctionResultOutput) Architectures() FunctionArchitecturesItemArrayOutput {
	return o.ApplyT(func(v LookupFunctionResult) []FunctionArchitecturesItem { return v.Architectures }).(FunctionArchitecturesItemArrayOutput)
}

// Unique identifier for function resources
func (o LookupFunctionResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// A unique Arn for CodeSigningConfig resource
func (o LookupFunctionResultOutput) CodeSigningConfigArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *string { return v.CodeSigningConfigArn }).(pulumi.StringPtrOutput)
}

// A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
func (o LookupFunctionResultOutput) DeadLetterConfig() FunctionDeadLetterConfigPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionDeadLetterConfig { return v.DeadLetterConfig }).(FunctionDeadLetterConfigPtrOutput)
}

// A description of the function.
func (o LookupFunctionResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Environment variables that are accessible from function code during execution.
func (o LookupFunctionResultOutput) Environment() FunctionEnvironmentPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionEnvironment { return v.Environment }).(FunctionEnvironmentPtrOutput)
}

// A function's ephemeral storage settings.
func (o LookupFunctionResultOutput) EphemeralStorage() FunctionEphemeralStoragePtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionEphemeralStorage { return v.EphemeralStorage }).(FunctionEphemeralStoragePtrOutput)
}

// Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
func (o LookupFunctionResultOutput) FileSystemConfigs() FunctionFileSystemConfigArrayOutput {
	return o.ApplyT(func(v LookupFunctionResult) []FunctionFileSystemConfig { return v.FileSystemConfigs }).(FunctionFileSystemConfigArrayOutput)
}

// The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
func (o LookupFunctionResultOutput) Handler() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *string { return v.Handler }).(pulumi.StringPtrOutput)
}

// ImageConfig
func (o LookupFunctionResultOutput) ImageConfig() FunctionImageConfigPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionImageConfig { return v.ImageConfig }).(FunctionImageConfigPtrOutput)
}

// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
func (o LookupFunctionResultOutput) KmsKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *string { return v.KmsKeyArn }).(pulumi.StringPtrOutput)
}

// A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
func (o LookupFunctionResultOutput) Layers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupFunctionResult) []string { return v.Layers }).(pulumi.StringArrayOutput)
}

// The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
func (o LookupFunctionResultOutput) MemorySize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *int { return v.MemorySize }).(pulumi.IntPtrOutput)
}

// PackageType.
func (o LookupFunctionResultOutput) PackageType() FunctionPackageTypePtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionPackageType { return v.PackageType }).(FunctionPackageTypePtrOutput)
}

// The number of simultaneous executions to reserve for the function.
func (o LookupFunctionResultOutput) ReservedConcurrentExecutions() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *int { return v.ReservedConcurrentExecutions }).(pulumi.IntPtrOutput)
}

// The Amazon Resource Name (ARN) of the function's execution role.
func (o LookupFunctionResultOutput) Role() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *string { return v.Role }).(pulumi.StringPtrOutput)
}

// The identifier of the function's runtime.
func (o LookupFunctionResultOutput) Runtime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *string { return v.Runtime }).(pulumi.StringPtrOutput)
}

// RuntimeManagementConfig
func (o LookupFunctionResultOutput) RuntimeManagementConfig() FunctionRuntimeManagementConfigPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionRuntimeManagementConfig { return v.RuntimeManagementConfig }).(FunctionRuntimeManagementConfigPtrOutput)
}

// The SnapStart setting of your function
func (o LookupFunctionResultOutput) SnapStart() FunctionSnapStartPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionSnapStart { return v.SnapStart }).(FunctionSnapStartPtrOutput)
}

// The SnapStart response of your function
func (o LookupFunctionResultOutput) SnapStartResponse() FunctionSnapStartResponsePtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionSnapStartResponse { return v.SnapStartResponse }).(FunctionSnapStartResponsePtrOutput)
}

// A list of tags to apply to the function.
func (o LookupFunctionResultOutput) Tags() FunctionTagArrayOutput {
	return o.ApplyT(func(v LookupFunctionResult) []FunctionTag { return v.Tags }).(FunctionTagArrayOutput)
}

// The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
func (o LookupFunctionResultOutput) Timeout() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *int { return v.Timeout }).(pulumi.IntPtrOutput)
}

// Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
func (o LookupFunctionResultOutput) TracingConfig() FunctionTracingConfigPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionTracingConfig { return v.TracingConfig }).(FunctionTracingConfigPtrOutput)
}

// For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
func (o LookupFunctionResultOutput) VpcConfig() FunctionVpcConfigPtrOutput {
	return o.ApplyT(func(v LookupFunctionResult) *FunctionVpcConfig { return v.VpcConfig }).(FunctionVpcConfigPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupFunctionResultOutput{})
}
