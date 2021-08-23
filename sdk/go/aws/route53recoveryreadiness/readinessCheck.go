// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package route53recoveryreadiness

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html
type ReadinessCheck struct {
	pulumi.CustomResourceState

	ReadinessCheckArn pulumi.StringOutput `pulumi:"readinessCheckArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname
	ReadinessCheckName pulumi.StringOutput `pulumi:"readinessCheckName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname
	ResourceSetName pulumi.StringPtrOutput `pulumi:"resourceSetName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewReadinessCheck registers a new resource with the given unique name, arguments, and options.
func NewReadinessCheck(ctx *pulumi.Context,
	name string, args *ReadinessCheckArgs, opts ...pulumi.ResourceOption) (*ReadinessCheck, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ReadinessCheckName == nil {
		return nil, errors.New("invalid value for required argument 'ReadinessCheckName'")
	}
	var resource ReadinessCheck
	err := ctx.RegisterResource("aws-native:route53recoveryreadiness:ReadinessCheck", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetReadinessCheck gets an existing ReadinessCheck resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReadinessCheck(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ReadinessCheckState, opts ...pulumi.ResourceOption) (*ReadinessCheck, error) {
	var resource ReadinessCheck
	err := ctx.ReadResource("aws-native:route53recoveryreadiness:ReadinessCheck", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ReadinessCheck resources.
type readinessCheckState struct {
}

type ReadinessCheckState struct {
}

func (ReadinessCheckState) ElementType() reflect.Type {
	return reflect.TypeOf((*readinessCheckState)(nil)).Elem()
}

type readinessCheckArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname
	ReadinessCheckName string `pulumi:"readinessCheckName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname
	ResourceSetName *string `pulumi:"resourceSetName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a ReadinessCheck resource.
type ReadinessCheckArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname
	ReadinessCheckName pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname
	ResourceSetName pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags
	Tags aws.TagArrayInput
}

func (ReadinessCheckArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*readinessCheckArgs)(nil)).Elem()
}

type ReadinessCheckInput interface {
	pulumi.Input

	ToReadinessCheckOutput() ReadinessCheckOutput
	ToReadinessCheckOutputWithContext(ctx context.Context) ReadinessCheckOutput
}

func (*ReadinessCheck) ElementType() reflect.Type {
	return reflect.TypeOf((*ReadinessCheck)(nil))
}

func (i *ReadinessCheck) ToReadinessCheckOutput() ReadinessCheckOutput {
	return i.ToReadinessCheckOutputWithContext(context.Background())
}

func (i *ReadinessCheck) ToReadinessCheckOutputWithContext(ctx context.Context) ReadinessCheckOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReadinessCheckOutput)
}

type ReadinessCheckOutput struct{ *pulumi.OutputState }

func (ReadinessCheckOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ReadinessCheck)(nil))
}

func (o ReadinessCheckOutput) ToReadinessCheckOutput() ReadinessCheckOutput {
	return o
}

func (o ReadinessCheckOutput) ToReadinessCheckOutputWithContext(ctx context.Context) ReadinessCheckOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ReadinessCheckOutput{})
}
