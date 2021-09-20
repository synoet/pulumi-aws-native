// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package imagebuilder

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::ImageBuilder::ImagePipeline
type ImagePipeline struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the image pipeline.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
	ContainerRecipeArn pulumi.StringPtrOutput `pulumi:"containerRecipeArn"`
	// The description of the image pipeline.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
	DistributionConfigurationArn pulumi.StringPtrOutput `pulumi:"distributionConfigurationArn"`
	// Collects additional information about the image being created, including the operating system (OS) version and package list.
	EnhancedImageMetadataEnabled pulumi.BoolPtrOutput `pulumi:"enhancedImageMetadataEnabled"`
	// The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
	ImageRecipeArn pulumi.StringPtrOutput `pulumi:"imageRecipeArn"`
	// The image tests configuration of the image pipeline.
	ImageTestsConfiguration ImagePipelineImageTestsConfigurationPtrOutput `pulumi:"imageTestsConfiguration"`
	// The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
	InfrastructureConfigurationArn pulumi.StringPtrOutput `pulumi:"infrastructureConfigurationArn"`
	// The name of the image pipeline.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// The schedule of the image pipeline.
	Schedule ImagePipelineSchedulePtrOutput `pulumi:"schedule"`
	// The status of the image pipeline.
	Status ImagePipelineStatusPtrOutput `pulumi:"status"`
	// The tags of this image pipeline.
	Tags pulumi.AnyOutput `pulumi:"tags"`
}

// NewImagePipeline registers a new resource with the given unique name, arguments, and options.
func NewImagePipeline(ctx *pulumi.Context,
	name string, args *ImagePipelineArgs, opts ...pulumi.ResourceOption) (*ImagePipeline, error) {
	if args == nil {
		args = &ImagePipelineArgs{}
	}

	var resource ImagePipeline
	err := ctx.RegisterResource("aws-native:imagebuilder:ImagePipeline", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetImagePipeline gets an existing ImagePipeline resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetImagePipeline(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ImagePipelineState, opts ...pulumi.ResourceOption) (*ImagePipeline, error) {
	var resource ImagePipeline
	err := ctx.ReadResource("aws-native:imagebuilder:ImagePipeline", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ImagePipeline resources.
type imagePipelineState struct {
}

type ImagePipelineState struct {
}

func (ImagePipelineState) ElementType() reflect.Type {
	return reflect.TypeOf((*imagePipelineState)(nil)).Elem()
}

type imagePipelineArgs struct {
	// The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
	ContainerRecipeArn *string `pulumi:"containerRecipeArn"`
	// The description of the image pipeline.
	Description *string `pulumi:"description"`
	// The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
	DistributionConfigurationArn *string `pulumi:"distributionConfigurationArn"`
	// Collects additional information about the image being created, including the operating system (OS) version and package list.
	EnhancedImageMetadataEnabled *bool `pulumi:"enhancedImageMetadataEnabled"`
	// The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
	ImageRecipeArn *string `pulumi:"imageRecipeArn"`
	// The image tests configuration of the image pipeline.
	ImageTestsConfiguration *ImagePipelineImageTestsConfiguration `pulumi:"imageTestsConfiguration"`
	// The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
	InfrastructureConfigurationArn *string `pulumi:"infrastructureConfigurationArn"`
	// The name of the image pipeline.
	Name *string `pulumi:"name"`
	// The schedule of the image pipeline.
	Schedule *ImagePipelineSchedule `pulumi:"schedule"`
	// The status of the image pipeline.
	Status *ImagePipelineStatus `pulumi:"status"`
	// The tags of this image pipeline.
	Tags interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a ImagePipeline resource.
type ImagePipelineArgs struct {
	// The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
	ContainerRecipeArn pulumi.StringPtrInput
	// The description of the image pipeline.
	Description pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
	DistributionConfigurationArn pulumi.StringPtrInput
	// Collects additional information about the image being created, including the operating system (OS) version and package list.
	EnhancedImageMetadataEnabled pulumi.BoolPtrInput
	// The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
	ImageRecipeArn pulumi.StringPtrInput
	// The image tests configuration of the image pipeline.
	ImageTestsConfiguration ImagePipelineImageTestsConfigurationPtrInput
	// The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
	InfrastructureConfigurationArn pulumi.StringPtrInput
	// The name of the image pipeline.
	Name pulumi.StringPtrInput
	// The schedule of the image pipeline.
	Schedule ImagePipelineSchedulePtrInput
	// The status of the image pipeline.
	Status ImagePipelineStatusPtrInput
	// The tags of this image pipeline.
	Tags pulumi.Input
}

func (ImagePipelineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*imagePipelineArgs)(nil)).Elem()
}

type ImagePipelineInput interface {
	pulumi.Input

	ToImagePipelineOutput() ImagePipelineOutput
	ToImagePipelineOutputWithContext(ctx context.Context) ImagePipelineOutput
}

func (*ImagePipeline) ElementType() reflect.Type {
	return reflect.TypeOf((*ImagePipeline)(nil))
}

func (i *ImagePipeline) ToImagePipelineOutput() ImagePipelineOutput {
	return i.ToImagePipelineOutputWithContext(context.Background())
}

func (i *ImagePipeline) ToImagePipelineOutputWithContext(ctx context.Context) ImagePipelineOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ImagePipelineOutput)
}

type ImagePipelineOutput struct{ *pulumi.OutputState }

func (ImagePipelineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ImagePipeline)(nil))
}

func (o ImagePipelineOutput) ToImagePipelineOutput() ImagePipelineOutput {
	return o
}

func (o ImagePipelineOutput) ToImagePipelineOutputWithContext(ctx context.Context) ImagePipelineOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ImagePipelineOutput{})
}
