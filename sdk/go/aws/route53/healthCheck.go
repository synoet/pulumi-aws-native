// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package route53

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html
type HealthCheck struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig
	HealthCheckConfig pulumi.AnyOutput    `pulumi:"healthCheckConfig"`
	HealthCheckId     pulumi.StringOutput `pulumi:"healthCheckId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags
	HealthCheckTags HealthCheckHealthCheckTagArrayOutput `pulumi:"healthCheckTags"`
}

// NewHealthCheck registers a new resource with the given unique name, arguments, and options.
func NewHealthCheck(ctx *pulumi.Context,
	name string, args *HealthCheckArgs, opts ...pulumi.ResourceOption) (*HealthCheck, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.HealthCheckConfig == nil {
		return nil, errors.New("invalid value for required argument 'HealthCheckConfig'")
	}
	var resource HealthCheck
	err := ctx.RegisterResource("aws-native:route53:HealthCheck", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHealthCheck gets an existing HealthCheck resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHealthCheck(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HealthCheckState, opts ...pulumi.ResourceOption) (*HealthCheck, error) {
	var resource HealthCheck
	err := ctx.ReadResource("aws-native:route53:HealthCheck", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HealthCheck resources.
type healthCheckState struct {
}

type HealthCheckState struct {
}

func (HealthCheckState) ElementType() reflect.Type {
	return reflect.TypeOf((*healthCheckState)(nil)).Elem()
}

type healthCheckArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig
	HealthCheckConfig interface{} `pulumi:"healthCheckConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags
	HealthCheckTags []HealthCheckHealthCheckTag `pulumi:"healthCheckTags"`
}

// The set of arguments for constructing a HealthCheck resource.
type HealthCheckArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig
	HealthCheckConfig pulumi.Input
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags
	HealthCheckTags HealthCheckHealthCheckTagArrayInput
}

func (HealthCheckArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*healthCheckArgs)(nil)).Elem()
}

type HealthCheckInput interface {
	pulumi.Input

	ToHealthCheckOutput() HealthCheckOutput
	ToHealthCheckOutputWithContext(ctx context.Context) HealthCheckOutput
}

func (*HealthCheck) ElementType() reflect.Type {
	return reflect.TypeOf((*HealthCheck)(nil))
}

func (i *HealthCheck) ToHealthCheckOutput() HealthCheckOutput {
	return i.ToHealthCheckOutputWithContext(context.Background())
}

func (i *HealthCheck) ToHealthCheckOutputWithContext(ctx context.Context) HealthCheckOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HealthCheckOutput)
}

type HealthCheckOutput struct{ *pulumi.OutputState }

func (HealthCheckOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*HealthCheck)(nil))
}

func (o HealthCheckOutput) ToHealthCheckOutput() HealthCheckOutput {
	return o
}

func (o HealthCheckOutput) ToHealthCheckOutputWithContext(ctx context.Context) HealthCheckOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(HealthCheckOutput{})
}
