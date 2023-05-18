// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package guardduty

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::GuardDuty::IPSet
//
// Deprecated: IPSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type IPSet struct {
	pulumi.CustomResourceState

	Activate   pulumi.BoolOutput      `pulumi:"activate"`
	DetectorId pulumi.StringOutput    `pulumi:"detectorId"`
	Format     pulumi.StringOutput    `pulumi:"format"`
	Location   pulumi.StringOutput    `pulumi:"location"`
	Name       pulumi.StringPtrOutput `pulumi:"name"`
	Tags       IPSetTagArrayOutput    `pulumi:"tags"`
}

// NewIPSet registers a new resource with the given unique name, arguments, and options.
func NewIPSet(ctx *pulumi.Context,
	name string, args *IPSetArgs, opts ...pulumi.ResourceOption) (*IPSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Activate == nil {
		return nil, errors.New("invalid value for required argument 'Activate'")
	}
	if args.DetectorId == nil {
		return nil, errors.New("invalid value for required argument 'DetectorId'")
	}
	if args.Format == nil {
		return nil, errors.New("invalid value for required argument 'Format'")
	}
	if args.Location == nil {
		return nil, errors.New("invalid value for required argument 'Location'")
	}
	var resource IPSet
	err := ctx.RegisterResource("aws-native:guardduty:IPSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIPSet gets an existing IPSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIPSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IPSetState, opts ...pulumi.ResourceOption) (*IPSet, error) {
	var resource IPSet
	err := ctx.ReadResource("aws-native:guardduty:IPSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IPSet resources.
type ipsetState struct {
}

type IPSetState struct {
}

func (IPSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipsetState)(nil)).Elem()
}

type ipsetArgs struct {
	Activate   bool       `pulumi:"activate"`
	DetectorId string     `pulumi:"detectorId"`
	Format     string     `pulumi:"format"`
	Location   string     `pulumi:"location"`
	Name       *string    `pulumi:"name"`
	Tags       []IPSetTag `pulumi:"tags"`
}

// The set of arguments for constructing a IPSet resource.
type IPSetArgs struct {
	Activate   pulumi.BoolInput
	DetectorId pulumi.StringInput
	Format     pulumi.StringInput
	Location   pulumi.StringInput
	Name       pulumi.StringPtrInput
	Tags       IPSetTagArrayInput
}

func (IPSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipsetArgs)(nil)).Elem()
}

type IPSetInput interface {
	pulumi.Input

	ToIPSetOutput() IPSetOutput
	ToIPSetOutputWithContext(ctx context.Context) IPSetOutput
}

func (*IPSet) ElementType() reflect.Type {
	return reflect.TypeOf((**IPSet)(nil)).Elem()
}

func (i *IPSet) ToIPSetOutput() IPSetOutput {
	return i.ToIPSetOutputWithContext(context.Background())
}

func (i *IPSet) ToIPSetOutputWithContext(ctx context.Context) IPSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPSetOutput)
}

type IPSetOutput struct{ *pulumi.OutputState }

func (IPSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IPSet)(nil)).Elem()
}

func (o IPSetOutput) ToIPSetOutput() IPSetOutput {
	return o
}

func (o IPSetOutput) ToIPSetOutputWithContext(ctx context.Context) IPSetOutput {
	return o
}

func (o IPSetOutput) Activate() pulumi.BoolOutput {
	return o.ApplyT(func(v *IPSet) pulumi.BoolOutput { return v.Activate }).(pulumi.BoolOutput)
}

func (o IPSetOutput) DetectorId() pulumi.StringOutput {
	return o.ApplyT(func(v *IPSet) pulumi.StringOutput { return v.DetectorId }).(pulumi.StringOutput)
}

func (o IPSetOutput) Format() pulumi.StringOutput {
	return o.ApplyT(func(v *IPSet) pulumi.StringOutput { return v.Format }).(pulumi.StringOutput)
}

func (o IPSetOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *IPSet) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

func (o IPSetOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *IPSet) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o IPSetOutput) Tags() IPSetTagArrayOutput {
	return o.ApplyT(func(v *IPSet) IPSetTagArrayOutput { return v.Tags }).(IPSetTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IPSetInput)(nil)).Elem(), &IPSet{})
	pulumi.RegisterOutputType(IPSetOutput{})
}
