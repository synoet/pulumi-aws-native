// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package guardduty

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::GuardDuty::Member
//
// Deprecated: Member is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Member struct {
	pulumi.CustomResourceState

	DetectorId               pulumi.StringOutput    `pulumi:"detectorId"`
	DisableEmailNotification pulumi.BoolPtrOutput   `pulumi:"disableEmailNotification"`
	Email                    pulumi.StringOutput    `pulumi:"email"`
	MemberId                 pulumi.StringOutput    `pulumi:"memberId"`
	Message                  pulumi.StringPtrOutput `pulumi:"message"`
	Status                   pulumi.StringPtrOutput `pulumi:"status"`
}

// NewMember registers a new resource with the given unique name, arguments, and options.
func NewMember(ctx *pulumi.Context,
	name string, args *MemberArgs, opts ...pulumi.ResourceOption) (*Member, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DetectorId == nil {
		return nil, errors.New("invalid value for required argument 'DetectorId'")
	}
	if args.Email == nil {
		return nil, errors.New("invalid value for required argument 'Email'")
	}
	if args.MemberId == nil {
		return nil, errors.New("invalid value for required argument 'MemberId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"detectorId",
		"email",
		"memberId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Member
	err := ctx.RegisterResource("aws-native:guardduty:Member", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMember gets an existing Member resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MemberState, opts ...pulumi.ResourceOption) (*Member, error) {
	var resource Member
	err := ctx.ReadResource("aws-native:guardduty:Member", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Member resources.
type memberState struct {
}

type MemberState struct {
}

func (MemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*memberState)(nil)).Elem()
}

type memberArgs struct {
	DetectorId               string  `pulumi:"detectorId"`
	DisableEmailNotification *bool   `pulumi:"disableEmailNotification"`
	Email                    string  `pulumi:"email"`
	MemberId                 string  `pulumi:"memberId"`
	Message                  *string `pulumi:"message"`
	Status                   *string `pulumi:"status"`
}

// The set of arguments for constructing a Member resource.
type MemberArgs struct {
	DetectorId               pulumi.StringInput
	DisableEmailNotification pulumi.BoolPtrInput
	Email                    pulumi.StringInput
	MemberId                 pulumi.StringInput
	Message                  pulumi.StringPtrInput
	Status                   pulumi.StringPtrInput
}

func (MemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*memberArgs)(nil)).Elem()
}

type MemberInput interface {
	pulumi.Input

	ToMemberOutput() MemberOutput
	ToMemberOutputWithContext(ctx context.Context) MemberOutput
}

func (*Member) ElementType() reflect.Type {
	return reflect.TypeOf((**Member)(nil)).Elem()
}

func (i *Member) ToMemberOutput() MemberOutput {
	return i.ToMemberOutputWithContext(context.Background())
}

func (i *Member) ToMemberOutputWithContext(ctx context.Context) MemberOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MemberOutput)
}

type MemberOutput struct{ *pulumi.OutputState }

func (MemberOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Member)(nil)).Elem()
}

func (o MemberOutput) ToMemberOutput() MemberOutput {
	return o
}

func (o MemberOutput) ToMemberOutputWithContext(ctx context.Context) MemberOutput {
	return o
}

func (o MemberOutput) DetectorId() pulumi.StringOutput {
	return o.ApplyT(func(v *Member) pulumi.StringOutput { return v.DetectorId }).(pulumi.StringOutput)
}

func (o MemberOutput) DisableEmailNotification() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Member) pulumi.BoolPtrOutput { return v.DisableEmailNotification }).(pulumi.BoolPtrOutput)
}

func (o MemberOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v *Member) pulumi.StringOutput { return v.Email }).(pulumi.StringOutput)
}

func (o MemberOutput) MemberId() pulumi.StringOutput {
	return o.ApplyT(func(v *Member) pulumi.StringOutput { return v.MemberId }).(pulumi.StringOutput)
}

func (o MemberOutput) Message() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Member) pulumi.StringPtrOutput { return v.Message }).(pulumi.StringPtrOutput)
}

func (o MemberOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Member) pulumi.StringPtrOutput { return v.Status }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MemberInput)(nil)).Elem(), &Member{})
	pulumi.RegisterOutputType(MemberOutput{})
}
