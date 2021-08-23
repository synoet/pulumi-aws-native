// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package route53recoverycontrol

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html
type ControlPanel struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn
	ClusterArn          pulumi.StringPtrOutput `pulumi:"clusterArn"`
	ControlPanelArn     pulumi.StringOutput    `pulumi:"controlPanelArn"`
	DefaultControlPanel pulumi.BoolOutput      `pulumi:"defaultControlPanel"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name
	Name                pulumi.StringOutput `pulumi:"name"`
	RoutingControlCount pulumi.IntOutput    `pulumi:"routingControlCount"`
	Status              pulumi.StringOutput `pulumi:"status"`
}

// NewControlPanel registers a new resource with the given unique name, arguments, and options.
func NewControlPanel(ctx *pulumi.Context,
	name string, args *ControlPanelArgs, opts ...pulumi.ResourceOption) (*ControlPanel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource ControlPanel
	err := ctx.RegisterResource("aws-native:route53recoverycontrol:ControlPanel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetControlPanel gets an existing ControlPanel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetControlPanel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ControlPanelState, opts ...pulumi.ResourceOption) (*ControlPanel, error) {
	var resource ControlPanel
	err := ctx.ReadResource("aws-native:route53recoverycontrol:ControlPanel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ControlPanel resources.
type controlPanelState struct {
}

type ControlPanelState struct {
}

func (ControlPanelState) ElementType() reflect.Type {
	return reflect.TypeOf((*controlPanelState)(nil)).Elem()
}

type controlPanelArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn
	ClusterArn *string `pulumi:"clusterArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name
	Name string `pulumi:"name"`
}

// The set of arguments for constructing a ControlPanel resource.
type ControlPanelArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn
	ClusterArn pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name
	Name pulumi.StringInput
}

func (ControlPanelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*controlPanelArgs)(nil)).Elem()
}

type ControlPanelInput interface {
	pulumi.Input

	ToControlPanelOutput() ControlPanelOutput
	ToControlPanelOutputWithContext(ctx context.Context) ControlPanelOutput
}

func (*ControlPanel) ElementType() reflect.Type {
	return reflect.TypeOf((*ControlPanel)(nil))
}

func (i *ControlPanel) ToControlPanelOutput() ControlPanelOutput {
	return i.ToControlPanelOutputWithContext(context.Background())
}

func (i *ControlPanel) ToControlPanelOutputWithContext(ctx context.Context) ControlPanelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ControlPanelOutput)
}

type ControlPanelOutput struct{ *pulumi.OutputState }

func (ControlPanelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ControlPanel)(nil))
}

func (o ControlPanelOutput) ToControlPanelOutput() ControlPanelOutput {
	return o
}

func (o ControlPanelOutput) ToControlPanelOutputWithContext(ctx context.Context) ControlPanelOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ControlPanelOutput{})
}
